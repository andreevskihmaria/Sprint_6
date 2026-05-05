from selenium.webdriver.common.by import By


#локаторы на главной страницы
class MainPageLocators:
    BUTTON_ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav__AGCXC')]//button[text()='Заказать']")#кнопка "Заказать" вверху страницы
    BUTTON_ORDER_HOME = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//button[text()='Заказать']")#кнопка "Заказать" внизу страницы
    LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI") #лого "Яндекс"
    QUESTIONS_TITLE = (By.XPATH, "//div[text()='Вопросы о важном']") #"Вопросы о важном"
    BUTTON_COOKIES = (By.CLASS_NAME, 'App_CookieButton__3cvqF')

    @staticmethod
    def question_button(number):
        return (By.ID, f"accordion__heading-{number}")
    
    @staticmethod
    def question_answer(number):
        return (By.ID, f"accordion__panel-{number}")


#локаторы на странице заказа
class OrderPageLocators:
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR") #лого "Самокат"
    NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder*="Имя"]')
    SURNAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder*="Фамилия"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[placeholder*="Адрес"]')
    METRO_FIELD = (By.CSS_SELECTOR, 'input[placeholder*="Станция метро"]')
    PHONE_FIELD = (By.CSS_SELECTOR, 'input[placeholder*="Телефон"]')
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = (By.CSS_SELECTOR, 'input[placeholder*="Когда привезти"]')
    RENTAL_PERIOD_INPUT = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]")

    @staticmethod
    def rent_period_option(text):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{text}']")
    
    COLOR_BLACK = (By.ID, 'black')
    COLOR_GREY = (By.ID, 'grey')
    COMMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Комментарий']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    BUTTON_CONFIRM_YES = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL_TEXT = (By.XPATH, '//div[text()="Заказ оформлен"]')
    TITLE_CONFIRMATION = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    METRO_FIRST_OPTION = (By.XPATH, ".//li[@class='select-search__row']")
