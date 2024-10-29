import pytest

from task3.framework.browser import Driver
from task3.config import settings


@pytest.fixture(autouse=True)
def get_browser_fixture():
    Driver().get_driver()
    yield
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
