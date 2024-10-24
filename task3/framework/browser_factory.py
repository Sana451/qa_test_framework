from selenium import webdriver

from task3.config import settings


class BrowserFactory:
    def __init__(self, browser_name):
        self.browser_name = browser_name

    def get_webdriver_instance(self):
        if self.browser_name == settings["chrome_name"]:
            driver = webdriver.Chrome(options=self.get_chrome_options())

        elif self.browser_name == settings["firefox_name"]:
            driver = webdriver.Firefox(options=self.get_firefox_options())

        else:
            raise Exception("Имя браузера указано неверно (возможные варианты: firefox)")

        driver.maximize_window()
        return driver

    @staticmethod
    def get_chrome_options():
        options = webdriver.ChromeOptions()
        options.add_argument(settings["chrome_incognito"])
        return options

    @staticmethod
    def get_firefox_options():
        options = webdriver.FirefoxOptions()
        options.add_argument(settings["firefox_private"])
        return options