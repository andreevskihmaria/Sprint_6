import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import URLS


@allure.feature('Логотипы')
class TestLogo:

    @allure.title('Проверка перехода на главную страницу Дзен при клике на логотип "Яндекс"')
    def test_logo_yandex(self, driver):
        page = MainPage(driver)
        page.open_mind_page()
        page.find_and_click_logo_yandex()
        page.switch_to_new_tab_and_wait_url(URLS.DZEN_URL)
        assert page.current_url_contains(URLS.DZEN_URL)


    @allure.title('Проверка перехода на главную страницу при клике на логотип "Самокат"')
    def test_logo_scooter(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.find_and_click_logo_scooter()
        page.check_url_to_be(URLS.MAIN_URL)
        assert page.current_url_contains(URLS.MAIN_URL)


