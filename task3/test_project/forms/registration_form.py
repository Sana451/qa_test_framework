from selenium.webdriver.common.by import By

from task3.framework.elements.base_element import BaseElement
from task3.framework.base_page import BasePage
from task3.framework.logger import Logger

log = Logger.__call__().get_logger()


class RegistrationForm(BasePage):
    __TITLE = (By.ID, "registration-form-modal")
    __FIRST_NAME_FIELD = (By.ID, "firstName")
    __LAST_NAME_FIELD = (By.ID, "lastName")
    __EMAIL_FIELD = (By.ID, "userEmail")
    __AGE_FIELD = (By.ID, "age")
    __SALARY_FIELD = (By.ID, "salary")
    __DEPARTMENT_FIELD = (By.ID, "department")
    __SUBMIT_BTN = (By.ID, "submit")

    def __init__(self):
        super().__init__(locator=(By.XPATH, "//*[contains(text(), 'Registration F')]"), name="RegistrationForm")

    @property
    def base_element(self):
        return BaseElement("", "BaseElement")

    def send_text_to_first_name_field(self, first_name):
        self.base_element.send_text_to_element(self.__FIRST_NAME_FIELD, first_name)

    def send_text_to_last_name_field(self, last_name):
        self.base_element.send_text_to_element(self.__LAST_NAME_FIELD, last_name)

    def send_text_to_email_field(self, email):
        self.base_element.send_text_to_element(self.__EMAIL_FIELD, email)

    def send_text_to_age_field(self, age):
        self.base_element.send_text_to_element(self.__AGE_FIELD, age)

    def send_text_to_salary_field(self, salary):
        self.base_element.send_text_to_element(self.__SALARY_FIELD, salary)

    def send_text_to_department_field(self, department):
        self.base_element.send_text_to_element(self.__DEPARTMENT_FIELD, department)

    def click_submit_btn(self):
        self.base_element.click_to_element(self.__SUBMIT_BTN)

    def register_user(self, user):
        self.send_text_to_first_name_field(user["first_name"])
        self.send_text_to_last_name_field(user["last_name"])
        self.send_text_to_email_field(user["email"])
        self.send_text_to_age_field(user["age"])
        self.send_text_to_salary_field(user["salary"])
        self.send_text_to_department_field(user["department"])
        log.info(f"{self.name} введены данные {user.values()}")
        self.click_submit_btn()
        log.info(f"{self.name} форма отправлена")

    def check_user_registered(self, user):
        __FIRST_NAME_TD = (By.XPATH, f"//*[@class='rt-td' and contains(text(), '{user['first_name']}')]")
        __LAST_NAME_TD = (By.XPATH, f"//*[@class='rt-td' and contains(text(), '{user['last_name']}')]")
        __AGE_TD = (By.XPATH, f"//*[@class='rt-td' and contains(text(), '{user['age']}')]")
        __EMAIL_TD = (By.XPATH, f"//*[@class='rt-td' and contains(text(), '{user['email']}')]")
        __SALARY_TD = (By.XPATH, f"//*[@class='rt-td' and contains(text(), '{user['salary']}')]")
        __DEPARTMENT_TD = (By.XPATH, f"//*[@class='rt-td' and contains(text(), '{user['department']}')]")

        if (
                self.base_element.element_is_displayed(__FIRST_NAME_TD) and
                self.base_element.element_is_displayed(__LAST_NAME_TD) and
                self.base_element.element_is_displayed(__AGE_TD) and
                self.base_element.element_is_displayed(__EMAIL_TD) and
                self.base_element.element_is_displayed(__SALARY_TD) and
                self.base_element.element_is_displayed(__DEPARTMENT_TD)
        ):
            log.debug(f"{self.name} удачная регистрации {user.values()}")
            return True
        else:
            log.debug(f"{self.name} неудачная регистрация {user.values()}")
            return False
