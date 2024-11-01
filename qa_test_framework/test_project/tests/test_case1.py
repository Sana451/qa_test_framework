import pytest

from qa_test_framework.config import settings
from qa_test_framework.test_project.pages.main_page import MainPage
from qa_test_framework.framework.test_tools.test_tools import GenRandomString
from qa_test_framework.framework.logger import Logger

log = Logger.__call__().get_logger()


@pytest.mark.usefixtures("get_browser_fixture")
class TestCase1Alerts:
    def test_case_1_alerts(self):
        log.info("\n>>>Запуск Testcase 1. Alerts<<<")
        main_page = MainPage()
        main_page.open_page(settings["main_page_url"])
        assert main_page.check_page_opened(), "Страница не открыта"

        main_page.click_alerts_frame_and_windows_btn()
        main_page.click_alerts_btn()
        assert main_page.alerts_form_on_page(), "На странице не появилась форма Alerts"

        main_page.click_alert_btn_click_me()
        assert main_page.get_alert_text() == settings["alert_btn_click_me_text"], \
            f"Alert с текстом {settings['alert_btn_click_me_text']} не открылся"

        main_page.accept_alert()
        assert main_page.check_alert_closed(), "Alert не закрылся"

        main_page.click_alert_btn_confirm_box()
        assert main_page.get_alert_text() == settings["alert_confirm_text"], \
            f"Alert с текстом {settings['alert_confirm_text']} не открылся"

        main_page.accept_alert()
        assert main_page.check_alert_closed() is True, "Alert не закрылся"

        main_page.click_alert_btn_prompt_box()
        assert main_page.get_alert_text() == settings["alert_btn_prompt_box_text"], \
            f"Alert с текстом {settings['alert_btn_prompt_box_text']} не открылся"

        random_string = GenRandomString.gen_by_len(10)
        main_page.send_text_to_prompt_box(random_string)
        main_page.accept_alert()
        assert main_page.check_alert_closed() is True, "Alert не закрылся"
        assert random_string in main_page.get_prompt_result_text(), "Текст не соответствует введённому в prompt"
