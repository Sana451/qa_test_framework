from selenium.webdriver.common.by import By

from task3.framework.base_page import BasePage
from task3.framework.browser import Driver
from task3.framework.elements.base_element import BaseElement
from task3.test_project.forms.registration_form import RegistrationForm
from task3.framework.logger import Logger

log = Logger.__call__().get_logger()


class MainPage(BasePage):
    __ALERTS_FRAME_AND_WINDOWS_BTN = (By.XPATH, "//*[contains(text(), 'Alerts, ')]")
    __ELEMENTS_BTN = (By.XPATH, "//*[(text()='Elements')]")
    __BROWSER_WINDOWS_BTN = (By.XPATH, "//*[text()='Browser Windows']")
    __ALERTS_BTN = (By.XPATH, "//*[text()='Alerts']")
    __FRAMES_BTN = (By.XPATH, "//*[text()='Frames']")
    __WEB_TABLES_BTN = (By.XPATH, "//*[text()='Web Tables']")
    __LINKS_BTN = (By.XPATH, "//*[text()='Links']")
    __WEB_TABLES_FORM = (By.XPATH, "//h1[text()='Web Tables']")
    __NESTED_FRAMES_BTN = (By.XPATH, "//*[text()='Nested Frames']")
    __ALERTS_FORM = (By.XPATH, "//*[@id='javascriptAlertsWrapper']")
    __FRAMES_FORM = (By.XPATH, "//*[@id='framesWrapper']")
    __ALERT_BTN_CLICK_ME = (By.XPATH, "//*[@id='alertButton']")
    __ALERT_BTN_CONFIRM_BOX = (By.XPATH, "//*[@id='confirmButton']")
    __ALERT_BTN_PROMPT_BOX = (By.XPATH, "//*[@id='promtButton']")
    __ALERT_PROMPT_RESULT = (By.XPATH, "//*[@id='promptResult']")
    __PARENT_FRAME_HOST = (By.XPATH, "//*[@id='frame1']")
    __PARENT_FRAME_TEXT = (By.XPATH, "//*[contains(text(), 'Parent frame')]")
    __CHILD_FRAME_HOST = (By.TAG_NAME, "iframe")
    __CHILD_FRAME_TEXT = (By.XPATH, "//*[contains(text(), 'Child Iframe')]")
    __UPPER_FRAME_HOST = (By.XPATH, "//*[@id='frame1Wrapper']//iframe")
    __LOWER_FRAME_HOST = (By.XPATH, "//*[@id='frame2Wrapper']//iframe")
    __UPPER_AND_LOWER_FRAME_TEXT = (By.XPATH, "//*[@id='sampleHeading']")
    __ADD_RECORD_BTN = (By.XPATH, "//*[@id='addNewRecordButton']")
    __REGISTRATION_FORM = (By.XPATH, "//*[contains(text(), 'Registration F')]")
    __DELETE_LAST_REGISTERED_USER_BTN = (By.XPATH, "(//*[@title='Delete'])[last()]")
    __COUNT_REGISTERED_USERS = (By.XPATH, "//*[@title='Delete']")
    __BROWSER_WINDOWS_FORM = (By.XPATH, "//*[@id='browserWindows']")
    __NEW_TAB_BTN = (By.XPATH, "//*[@id='tabButton']")
    __SAMPLE_PAGE_TEXT = (By.XPATH, "//*[contains(text(), 'sample page')]")
    __LINKS_PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Links')]")
    __HOME_LINK = (By.XPATH, "//*[@id='simpleLink']")

    def __init__(self):
        super().__init__(locator=(By.XPATH, "//*[@class='home-content']"), name="MainPage")

    @property
    def registration_form(self):
        return RegistrationForm()

    @property
    def base_element(self):
        return BaseElement("", "BaseElement")

    def open_page(self, url):
        Driver().get_driver().get(url)
        log.debug(f"{self.name} открыта")

    def check_page_opened(self):
        is_opened = self.base_element.find_element(self.locator).is_displayed()
        log.info(f"{self.name} открыта" if is_opened else f"{self.name} не открыта")
        return is_opened

    def click_alerts_frame_and_windows_btn(self):
        self.base_element.click_to_element(self.__ALERTS_FRAME_AND_WINDOWS_BTN)
        log.info(f"{self.name}: нажата alerts_frame_and_windows_btn")

    def click_elements_btn(self):
        self.base_element.click_to_element(self.__ELEMENTS_BTN)
        log.info(f"{self.name}: нажата elements_btn")

    def click_links_btn(self):
        self.base_element.click_to_element(self.__LINKS_BTN)
        log.info(f"{self.name}: нажата links_btn")

    def click_browser_windows_btn(self):
        self.base_element.click_to_element(self.__BROWSER_WINDOWS_BTN)
        log.info(f"{self.name}: нажата browser_windows_btn")

    def click_add_report_btn(self):
        self.base_element.click_to_element(self.__ADD_RECORD_BTN)
        log.info(f"{self.name}: нажата add_report_btn")

    def click_web_tables_btn(self):
        self.base_element.click_to_element(self.__WEB_TABLES_BTN)
        log.info(f"{self.name}: нажата web_tables_btn")

    def click_alerts_btn(self):
        self.base_element.click_to_element(self.__ALERTS_BTN)
        log.info(f"{self.name}: нажата alerts_btn")

    def click_nested_frames_btn(self):
        self.base_element.click_to_element(self.__NESTED_FRAMES_BTN)
        log.info(f"{self.name}: нажата nested_frames_btn")

    def click_frames_btn(self):
        self.base_element.click_to_element(self.__FRAMES_BTN)
        log.info(f"{self.name}: нажата frames_btn")

    def click_delete_last_register_user_btn(self):
        self.base_element.click_to_element(self.__DELETE_LAST_REGISTERED_USER_BTN)
        log.info(f"{self.name}: нажата delete_last_register_user_btn")

    def alerts_form_on_page(self):
        is_displayed = self.base_element.find_element(self.__ALERTS_FORM).is_displayed()
        log.info(f"{self.name}: форма 'alerts' на странице" if is_displayed
                 else f"{self.name}: форма 'alerts' не на странице")
        return is_displayed

    def frames_form_on_page(self):
        is_displayed = self.base_element.find_element(self.__FRAMES_FORM).is_displayed()
        log.info(f"{self.name}: форма 'frames' на странице" if is_displayed
                 else f"{self.name}: форма 'frames' не на странице")
        return is_displayed

    def browser_windows_form_on_page(self):
        is_displayed = self.base_element.find_element(self.__BROWSER_WINDOWS_FORM).is_displayed()
        log.info(f"{self.name}: форма 'browser_windows_form' на странице" if is_displayed
                 else f"{self.name}: форма 'browser_windows_form' не на странице")
        return is_displayed

    def web_tables_form_on_page(self):
        is_displayed = self.base_element.find_element(self.__WEB_TABLES_FORM).is_displayed()
        log.info(f"{self.name}: форма 'web_tables_form' на странице" if is_displayed
                 else f"{self.name}: форма 'web_tables_form' не на странице")
        return is_displayed

    def registration_form_on_page(self):
        is_displayed = self.base_element.find_element(self.__REGISTRATION_FORM).is_displayed()
        log.info(f"{self.name}: форма 'registration_form' на странице" if is_displayed
                 else f"{self.name}: форма 'registration_form' не на странице")
        return is_displayed

    def sample_text_on_page(self):
        is_displayed = self.base_element.find_element(self.__SAMPLE_PAGE_TEXT).is_displayed()
        log.info(f"{self.name}: 'sample_text' на странице" if is_displayed
                 else f"{self.name}: 'sample_text' не на странице")
        return is_displayed

    def links_form_on_page(self):
        is_displayed = self.base_element.find_element(self.__LINKS_PAGE_TITLE).is_displayed()
        log.info(f"{self.name}: 'links_form' на странице" if is_displayed
                 else f"{self.name}: 'links_form' не на странице")
        return is_displayed

    def click_alert_btn_click_me(self):
        self.base_element.click_to_element(self.__ALERT_BTN_CLICK_ME)
        log.info(f"{self.name}: нажата alert_btn_click_me")

    def click_home_link(self):
        self.base_element.click_to_element(self.__HOME_LINK)
        Driver().switch_to_new_tab()
        log.info(f"{self.name}: нажата home_link")

    def click_new_tab_btn(self):
        self.base_element.click_to_element(self.__NEW_TAB_BTN)
        Driver().switch_to_new_tab()
        log.info(f"{self.name}: нажата new_tab_btn")

    def click_alert_btn_confirm_box(self):
        self.base_element.click_to_element(self.__ALERT_BTN_CONFIRM_BOX)
        log.info(f"{self.name}: нажата alert_btn_confirm_box")

    def click_alert_btn_prompt_box(self):
        self.base_element.click_to_element(self.__ALERT_BTN_PROMPT_BOX)
        log.info(f"{self.name}: нажата alert_btn_prompt_box")

    def get_prompt_result_text(self):
        text = self.base_element.get_text(self.__ALERT_PROMPT_RESULT)
        log.info(f"{self.name}: текст {text} отображен в prompt")
        return text

    def switch_to_parent_frame(self):
        self.base_element.switch_to_frame(self.__PARENT_FRAME_HOST)
        log.info(f"{self.name}: переключился на родительский frame")

    def switch_to_child_frame(self):
        self.base_element.switch_to_frame(self.__CHILD_FRAME_HOST)
        log.info(f"{self.name}: переключился на дочерний frame")

    def switch_to_upper_frame(self):
        self.base_element.switch_to_frame(self.__UPPER_FRAME_HOST)
        log.info(f"{self.name}: переключился на верхний frame")

    def switch_to_lower_frame(self):
        self.base_element.switch_to_frame(self.__LOWER_FRAME_HOST)
        log.info(f"{self.name}: переключился на нижний frame")

    def get_parent_frame_text(self):
        self.switch_to_parent_frame()
        text = self.base_element.get_text(self.__PARENT_FRAME_TEXT)
        self.base_element.switch_to_default_content()
        log.info(f"{self.name}: текст {text} отображен в родительском frame")
        return text

    def get_child_frame_text(self):
        self.switch_to_parent_frame()
        self.switch_to_child_frame()
        text = self.base_element.get_text(self.__CHILD_FRAME_TEXT)
        self.base_element.switch_to_default_content()
        log.info(f"{self.name}: текст {text} отображен в дочернем frame")
        return text

    def get_upper_frame_text(self):
        self.switch_to_upper_frame()
        text = self.base_element.get_text(self.__UPPER_AND_LOWER_FRAME_TEXT)
        self.base_element.switch_to_default_content()
        log.info(f"{self.name}: текст {text} отображен в верхнем frame")
        return text

    def get_lower_frame_text(self):
        self.switch_to_lower_frame()
        text = self.base_element.get_text(self.__UPPER_AND_LOWER_FRAME_TEXT)
        self.base_element.switch_to_default_content()
        log.info(f"{self.name}: текст {text} отображен в нижнем frame")
        return text

    def registered_users_count(self):
        count = self.base_element.get_elements_count(self.__COUNT_REGISTERED_USERS)
        log.info(f"{self.name}: всего зарегистрированных пользователей: {count} ")
        return count

    def get_alert_text(self):
        return Driver().get_alert_text()

    def accept_alert(self):
        Driver().accept_alert()

    def check_alert_closed(self):
        return Driver().check_alert_closed()

    def send_text_to_prompt_box(self, text):
        Driver().send_text_to_prompt(text)

    def get_tabs_count(self):
        return Driver().tabs_count()

    def close_current_tab(self):
        Driver().close_current_tab()

    def switch_to_default_tab(self):
        Driver().switch_to_default_tab()
