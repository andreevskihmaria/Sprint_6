from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    @allure.step('Поиск и ожидание элемента')
    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
    

    @allure.step('Проскроллить до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)


    @allure.step('Найти и кликнуть по элементу')
    def find_and_click_element(self, locator):
        self.find_element(locator).click()


    @allure.step('Вставляем текст в поле')
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
        return element


    @allure.step('Проверяем открытие нужной страницы')
    def check_url_to_be(self, url, time=5):
        WebDriverWait(self.driver, time).until(EC.url_to_be(url))

    
    @allure.step('Проверяем, что текущий url содержит ожидаемый текст')
    def current_url_contains(self, url_part):
        return url_part in self.driver.current_url


    @allure.step('Ожидание элемента')
    def wait_for_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))


    @allure.step('Переключиться на последнюю открытую вкладку и подождать пока не поменяется url')
    def switch_to_new_tab_and_wait_url(self, url, time=10):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, time).until(EC.url_contains(url))
