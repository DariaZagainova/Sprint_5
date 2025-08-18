from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestsLocators
from generator_data import generation_data
from curl import Urls

# Регистрация, позитивные тесты
class TestRegistrationUser:

    # Проверка успешной регистрации с вводом корректных данных (Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен. Минимальный пароль — шесть символов.)
    def test_registration_all_fields_correct_input_success(self, go_to_registration_page):

        driver = go_to_registration_page
        name, email, password = generation_data()

        driver.find_element(*TestsLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*TestsLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestsLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestsLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.LOGIN_BUTTON))

        assert driver.current_url == Urls.LOGIN_PAGE

# Регистрация,негативные тесты
class TestRegistrationErrorPasword:

    # Проверка ошибки при вводе некорректного пароля (из 5 символов)
    def test_registration_error_password_show_error(self, go_to_registration_page):

        driver = go_to_registration_page
        name, email, password = generation_data()

        driver.find_element(*TestsLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*TestsLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestsLocators.PASSWORD_INPUT).send_keys(password[:5])
        driver.find_element(*TestsLocators.REGISTER_BUTTON).click()

        error_password = driver.find_elements(*TestsLocators.ERROR_PASSWORD_TEXT)
        assert len(error_password) > 0
