import pytest
import allure
from pages.main_page import MainPage
from data import test_data_expected_answer


@allure.feature('Тысты раздела "Вопросы о важном"')
class TestQuestion:
    
    @allure.title('Проверка ответа на вопрос №{index}')
    @allure.description('Открывается соответствующий текст при нажатии на стрелку вопроса')
    @pytest.mark.parametrize ("index, expected", test_data_expected_answer.items())
    def test_question_answer(self, driver, index, expected):
        page = MainPage(driver)
        page.open_mind_page()
        page.wait_main_page_loaded()
        page.scroll_to_faq()
        page.find_and_click_question(index)
        actual = page.get_answer_text(index)
        assert actual == expected    
