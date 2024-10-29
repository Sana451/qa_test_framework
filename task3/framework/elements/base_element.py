from selenium.common import (TimeoutException,
                             ElementNotInteractableException,
                             ElementClickInterceptedException)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from task3.config import settings
from task3.framework.browser import Driver
from task3.framework.logger import Logger
from task3.framework.scripts import Script

log = Logger.__call__().get_logger()


class BaseElement:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def find_element(self, locator):
        try:
            return WebDriverWait(Driver().get_driver(), settings["default_timeout"]).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException as exc:
            log.debug(f"{self.name} not found {locator} because TimeoutException")
            return None

    def find_elements(self, locator):
        try:
            return WebDriverWait(Driver().get_driver(), settings["default_timeout"]).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException as exc:
            log.error(f"{self.name} find_elements with {locator} method returned TimeoutException")
            raise TimeoutException

    def get_elements_count(self, locator):
        count = len(self.find_elements(locator))
        log.debug(f"{self.name} get_elements_count with {locator} returned {count}")
        return count

    def get_text(self, locator):
        text = self.find_element(locator).text
        log.debug(f"{self.name} get_element_text with {locator} returned {text}")
        return text

    def element_is_displayed(self, locator):
        element = self.find_element(locator)
        if element:
            if element.is_displayed():
                log.debug(f"{self.name} element_is_displayed {locator} returned True")
                return True
            else:
                log.debug(f"{self.name} element_is_displayed {locator} returned False")
                return False

    def click_to_element(self, locator):
        try:
            self.find_clickable_element(locator).click()
            log.debug(f"{self.name} clicked element {locator}")
        except (ElementNotInteractableException, ElementClickInterceptedException) as exc:
            Driver().get_driver().execute_script(Script.CLICK_TO_ELEMENT, self.find_clickable_element(locator))
            log.debug(f"{self.name} clicked element {locator}")

    def find_clickable_element(self, locator):
        return WebDriverWait(Driver().get_driver(), settings["default_timeout"]).until(
            EC.element_to_be_clickable(locator)
        )

    def send_text_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)
        log.debug(f"{self.name} typed text: {text} to element {locator}")

    def switch_to_frame(self, locator):
        frame = self.find_element(locator)
        Driver().switch_to_iframe(frame)
        log.debug(f"{self.name} switched to frame")

    def switch_to_default_content(self):
        Driver().switch_to_default_content()
        log.debug(f"{self.name} switched to default content")

    def tabs_count(self):
        count = Driver().tabs_count()
        log.info(f"{self.name} counted {count} opened tabs")
        return count

    def close_current_tab(self):
        Driver().close_current_tab()
        log.info(f"{self.name} закрыл текущую вкладку")

    def switch_to_default_tab(self):
        Driver().switch_to_default_tab()
        log.info(f"{self.name} переключился на основную вкладку")
