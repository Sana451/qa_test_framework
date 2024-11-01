from selenium import webdriver

from task3.config import settings


class BrowserFactory:

    def get_webdriver_instance(self, browser_name):
        if browser_name == settings["chrome_name"]:
            driver = webdriver.Chrome(options=self.get_chrome_options())

        elif browser_name == settings["firefox_name"]:
            driver = webdriver.Firefox(options=BrowserFactory.get_firefox_options())

        else:
            raise Exception("Имя браузера указано неверно"
                            "возможные варианты запуска:"
                            "pytest --browser_name firefox"
                            "pytest --browser_name chrome")

        driver.maximize_window()
        driver.set_page_load_timeout(180)
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
