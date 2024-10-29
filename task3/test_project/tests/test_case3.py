import pytest

from task3.config import settings
from task3.test_project.pages.main_page import MainPage
from task3.framework.logger import Logger

log = Logger.__call__().get_logger()


@pytest.mark.usefixtures("get_browser_fixture")
@pytest.mark.parametrize("user", [(settings["user_1"]), (settings["user_2"])])
class TestCase3Tables:
    def test_case_3_tables(self, user):
        log.info("\n>>>Запуск Testcase 3. Tables<<<")
        main_page = MainPage()
        main_page.open_page(settings["main_page_url"])
        assert main_page.check_page_opened(), "Страница не открыта"

        main_page.click_elements_btn()
        main_page.click_web_tables_btn()
        assert main_page.web_tables_form_on_page(), "Страница с формой 'Web Tables' не открыта"

        main_page.click_add_report_btn()
        assert main_page.registration_form_on_page(), "На странице не появилась форма 'Registration Form'"

        main_page.registration_form.register_user(user)
        assert main_page.registration_form.check_user_registered(user) is True, "В таблице не появились данные user1"

        registered_users_before_del = main_page.registered_users_count()
        main_page.click_delete_last_register_user_btn()
        assert registered_users_before_del > main_page.registered_users_count(), "Кол-во записей в таблице не изменилось"
        assert main_page.registration_form.check_user_registered(user) is False, "Пользователь не удалился из таблицы"
