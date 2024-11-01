from qa_test_framework.framework.browser import Driver
from qa_test_framework.framework.logger import Logger

log = Logger.__call__().get_logger()


class BasePage:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def check_page_opened(self):
        is_opened = Driver().get_driver().find_element(self.locator).is_displayed()
        log.info(f"{self.name} открыта" if is_opened else f"{self.name} не открыта")
        return is_opened
