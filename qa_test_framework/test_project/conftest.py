import pytest

from qa_test_framework.framework.browser import Driver
from qa_test_framework.config import settings


@pytest.fixture(autouse=True)
def get_browser_fixture():
    driver = Driver().get_driver()
    driver.get(settings["main_page_url"])
    yield driver
    Driver().del_driver()


@pytest.fixture(scope="session", autouse=True)
def browser_name(pytestconfig):
    return pytestconfig.getoption("browser_name")


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        default=settings["browser_name"],
        choices=(settings["chrome_name"], settings["firefox_name"])
    )
