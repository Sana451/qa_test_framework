import pytest

from task3.config import settings
from task3.test_project.pages.main_page import MainPage
from task3.framework.logger import Logger

log = Logger.__call__().get_logger()


@pytest.mark.usefixtures("get_browser_fixture")
class TestCase4Handles:
    def test_case_4_handles(self):
        log.info("\n>>>Запуск Testcase 4. Handles<<<")
        main_page = MainPage()
        main_page.open_page(settings["main_page_url"])
        assert main_page.check_page_opened(), "Страница не открыта"

        main_page.click_alerts_frame_and_windows_btn()
        main_page.click_browser_windows_btn()
        assert main_page.browser_windows_form_on_page(), "Страница с формой 'Browser Windows' не открыта"

        tabs_count_before_open_new_tab = main_page.get_tabs_count()
        main_page.click_new_tab_btn()
        assert main_page.get_tabs_count() > tabs_count_before_open_new_tab, "Новая вкладка браузера не открылась"
        assert main_page.sample_text_on_page(), "Вкладка не содержит текста 'sample page'"

        main_page.close_current_tab()
        assert main_page.browser_windows_form_on_page(), "Страница с формой 'Browser Windows' не открыта"

        main_page.click_elements_btn()
        main_page.click_links_btn()
        assert main_page.links_form_on_page(), "Страница с формой 'Links' не открыта"
        tabs_count_before_open_new_tab = main_page.get_tabs_count()

        main_page.click_home_link()
        assert main_page.get_tabs_count() > tabs_count_before_open_new_tab, "Новая вкладка браузера не открылась"
        assert main_page.check_page_opened(), "Новая вкладка открыта не главной странице"

        main_page.switch_to_default_tab()
        assert main_page.links_form_on_page(), "Страница с формой 'Links' не открыта"
