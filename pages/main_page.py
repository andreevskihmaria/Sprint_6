from .base_page import BasePage
from locators import MainPageLocators
from urls import URLS
from selenium.webdriver.common.action_chains import ActionChains
import allure


class MainPage(BasePage):

    @allure.step('Открыть главную страницу и принять куки')
    def open_mind_page(self):
        self.driver.get(URLS.MAIN_URL)
        self.find_and_click_element(MainPageLocators.BUTTON_COOKIES)


    @allure.step('Найти и нажать на кнопку "Заказать" в верхней части')
    def find_and_click_button_order_header(self):
        self.find_and_click_element(MainPageLocators.BUTTON_ORDER_HEADER)


    @allure.step('Найти и нажать на кнопку "Заказать" в нижней части')
    def find_and_click_button_order_home(self):
        self.find_and_click_element(MainPageLocators.BUTTON_ORDER_HOME)


    @allure.step('Проверяем загрузку url главной страницы')
    def wait_main_page_loaded(self):
        self.check_url_to_be(URLS.MAIN_URL)


    @allure.step('Проскроллим до раздела "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_TITLE)


    @allure.step('Найти и нажать на вопрос')
    def find_and_click_question(self, index):
        locator = MainPageLocators.question_button(index)
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


    @allure.step('Получаем текст вопроса')
    def get_answer_text(self, index):
        locator = MainPageLocators.question_answer(index)
        element = self.wait_for_visibility(locator)
        return element.text
    

    @allure.step('Найти и нажать на логотип "Яндекс"')
    def find_and_click_logo_yandex(self):
        self.find_and_click_element(MainPageLocators.LOGO_YANDEX)
