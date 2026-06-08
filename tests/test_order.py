import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import test_data_user_1, test_data_user_2


@allure.feature('Заказ самоката')
class TestOrderPage:

    @allure.title('Успешное оформление заказа: кнопка "Заказать" в {button}, пользователь {user_data[name]}')
    @allure.description('Позитивный сценарий заказа самоката с разными точками входа и наборами данных')
    @pytest.mark.parametrize("button, user_data", [('header', test_data_user_1),
                                                   ('home',test_data_user_2)])
    def test_order(self, driver, button, user_data):
        main = MainPage(driver)
        main.open_mind_page()
        main.wait_main_page_loaded()

        if button == 'header':
            main.find_and_click_button_order_header()
        else:
            main.find_and_click_button_order_home()

        order = OrderPage(driver)
        order.wait_order_page_loaded()
        order.filling_first_form(name=user_data['name'],
                                 surname=user_data['surname'],
                                 address=user_data['address'],
                                 metro=user_data['metro'],
                                 phone=user_data['phone'])
        order.click_button_next()
        order.wait_for_socond_form()
        order.filling_second_form(date=user_data['date'],
                                  rent_period=user_data['rent_period'],
                                  color=user_data['color'],
                                  comment=user_data['comment'])
        order.click_button_order()
        order.check_confirm_modal()
        order.click_button_yes()

        assert order.is_success_modal_visible()

