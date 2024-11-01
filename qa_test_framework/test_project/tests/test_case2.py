import pytest

from qa_test_framework.config import settings
from qa_test_framework.test_project.pages.main_page import MainPage
from qa_test_framework.framework.logger import Logger

log = Logger.__call__().get_logger()


@pytest.mark.usefixtures("get_browser_fixture")
class TestCase2Iframe:
    def test_case_2_iframe(self):
        log.info("\n>>>Запуск Testcase 2. Iframe<<<")
        main_page = MainPage()
        main_page.open_page(settings["main_page_url"])
        assert main_page.check_page_opened(), "Страница не открыта"

        main_page.click_alerts_frame_and_windows_btn()
        main_page.click_nested_frames_btn()
        assert main_page.frames_form_on_page(), "Страница с формой Nested Frames не открыта"
        assert settings["parent_frame_text"] in main_page.get_parent_frame_text(), \
            f"В центре страницы отсутствует надпись {settings['parent_frame_text']}"
        assert settings["child_frame_text"] in main_page.get_child_frame_text(), \
            f"В центре страницы отсутствует надпись {settings['child_frame_text']}"

        main_page.click_frames_btn()
        assert main_page.get_upper_frame_text() == main_page.get_lower_frame_text(), \
            "Надпись верхнего фрейма не соответствует нижнему"
