from selenium.common import NoAlertPresentException

from task3.framework.singleton import Singleton
from task3.framework.browser_factory import BrowserFactory
from task3.framework.logger import Logger
from task3.config import settings

log = Logger.__call__().get_logger()


class Driver(metaclass=Singleton):

    def __init__(self):
        self.__driver = None

    def get_driver(self):
        if self.__driver is None:
            try:
                self.__driver = BrowserFactory().get_webdriver_instance(settings["browser_name"])
                return self.__driver
            except Exception:
                print("Ошибка инициализации экземпляра драйвера (Driver.get_driver)")
        return self.__driver

    def del_driver(self):
        if self.__driver is not None:
            self.get_driver().quit()
            self.__driver = None

    def check_alert_closed(self):
        is_closed = not Driver().switch_to_alert()
        log.debug(f"Driver check_alert_closed method return {is_closed}")
        return is_closed

    def switch_to_alert(self):
        try:
            self.__driver.switch_to.alert
            log.debug("Driver: переключился на alert")
            return True
        except NoAlertPresentException:
            log.debug("Driver не переключился на alert т.к. alert не найден")
            return False

    def get_alert_text(self):
        text = self.__driver.switch_to.alert.text
        log.debug(f"Driver: извлёк {text} из alert")
        return text

    def accept_alert(self):
        log.info("Driver: подтвердил alert")
        self.__driver.switch_to.alert.accept()

    def send_text_to_prompt(self, text):
        self.__driver.switch_to.alert.send_keys(text)
        log.info(f"Driver: вввёл текст: {text} в prompt")

    def switch_to_iframe(self, frame):
        self.__driver.switch_to.frame(frame)
        log.debug(f"Driver: переключился на frame")

    def switch_to_default_content(self):
        self.__driver.switch_to.default_content()
        log.debug(f"Driver: переключился на основной контент")

    def switch_to_new_tab(self):
        windows = self.__driver.window_handles
        self.__driver.switch_to.window(windows[-1])
        log.debug(f"Driver: переключился на новую вкладку")

    def close_current_tab(self):
        self.__driver.close()
        windows = self.__driver.window_handles
        self.__driver.switch_to.window(windows[-1])
        log.debug(f"Driver: закрыл текущую вкладку")

    def switch_to_default_tab(self):
        windows = self.__driver.window_handles
        self.__driver.switch_to.window(windows[0])
        log.debug(f"Driver: переключился на основной контент")

    def tabs_count(self):
        log.debug(f"Driver: на данный момент открыто {len(self.__driver.window_handles)} вкладок")
        return len(self.__driver.window_handles)
