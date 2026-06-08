from .base_page import BasePage
from locators import OrderPageLocators
from urls import URLS
from selenium.webdriver.common.keys import Keys
import allure


class OrderPage(BasePage):

    @allure.step('Открыть страницу заказа')
    def open_order_page(self):
        self.driver.get(URLS.ORDER_URL)


    @allure.step('Найти и нажать на логотип "Самокат"')
    def find_and_click_logo_scooter(self):
        self.find_and_click_element(OrderPageLocators.LOGO_SCOOTER)
    

    @allure.step('Проверка загрузки url страницы заказа')
    def wait_order_page_loaded(self):
        self.check_url_to_be(URLS.ORDER_URL)


    @allure.step('Заполнить поля первой анкеты')
    def filling_first_form(self, name, surname, address, metro, phone):
        self.enter_text(OrderPageLocators.NAME_FIELD, name)
        self.enter_text(OrderPageLocators.SURNAME_FIELD, surname)
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)
        self.enter_text(OrderPageLocators.METRO_FIELD, metro)
        self.find_and_click_element(OrderPageLocators.METRO_FIRST_OPTION)
        self.enter_text(OrderPageLocators.PHONE_FIELD, phone)


    @allure.step('Найти и нажать на кнопку "Далее"')
    def click_button_next(self):
        self.find_and_click_element(OrderPageLocators.BUTTON_NEXT)


    @allure.step('Пождаться загрузку второй анкеты')
    def wait_for_socond_form(self):
        self.find_element(OrderPageLocators.COMMENT_INPUT)


    @allure.step('Заполнить поля второй анкеты')
    def filling_second_form(self, date, rent_period, color, comment):
        self.enter_text(OrderPageLocators.DATE_INPUT, date).send_keys(Keys.ENTER)

        self.find_and_click_element(OrderPageLocators.RENTAL_PERIOD_INPUT)
        self.find_and_click_element(OrderPageLocators.rent_period_option(rent_period))

        if color == 'black':
            self.find_and_click_element(OrderPageLocators.COLOR_BLACK)
        elif color == 'grey':
            self.find_and_click_element(OrderPageLocators.COLOR_GREY)

        self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)


    @allure.step('Найти и нажать кнопку "Заказать"')
    def click_button_order(self):
        self.find_and_click_element(OrderPageLocators.ORDER_BUTTON)


    @allure.step('Убедиться, что открылось окно подтверждения заказа')
    def check_confirm_modal(self):
        self.find_element(OrderPageLocators.TITLE_CONFIRMATION)


    @allure.step('Найти и нажать кнопку "Да"')
    def click_button_yes(self):
        self.find_and_click_element(OrderPageLocators.BUTTON_CONFIRM_YES)


    @allure.step('Убедиться, что открылось окно "Заказ оформлен"')
    def is_success_modal_visible(self):
        element = self.wait_for_visibility(OrderPageLocators.SUCCESS_MODAL_TEXT)
        return element.is_displayed()
        
