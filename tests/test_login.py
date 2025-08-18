from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import Urls
from locators import TestsLocators

class TestLoginFromDifferentPages:

    # Функция авторизует пользователя по email-паролю и проверяет успешный вход. Используется во всех тестах класса.
    def login_user(self, driver, email, password):
        driver.find_element(*TestsLocators.EMAIL_INPUT_LOGIN).send_keys(email)      
        driver.find_element(*TestsLocators.PASSWORD_INPUT_LOGIN).send_keys(password)  
        driver.find_element(*TestsLocators.LOGIN_BUTTON).click()   
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.ORDER_BUTTON))

        assert driver.current_url == Urls.MAIN_PAGE


    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page_correct_input_login(self, open_site, registered_user):

        driver = open_site

        driver.find_element(*TestsLocators.ENTER_ACCOUNT_BUTTON).click()       
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.LOGIN_BUTTON))

        email, password = registered_user
        self.login_user(driver, email, password)


    # Вход через кнопку «Личный кабинет»
    def test_login_from_profile_button_correct_input_login(self, open_site, registered_user):

        driver = open_site

        driver.find_element(*TestsLocators.PERSONAL_ACCOUNT_BUTTON).click()       
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.LOGIN_BUTTON))

        email, password = registered_user
        self.login_user(driver, email, password)


    # Вход через кнопку в форме регистрации
    def test_login_from_registration_form_correct_input_login(self, go_to_registration_page, registered_user):

        driver =  go_to_registration_page
        driver.find_element(*TestsLocators.LOGIN_LINK_ON_REGISTRATION_PAGE).click()

        email, password = registered_user
        self.login_user(driver, email, password)


    # Вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_form_correct_input_login(self, go_to_registration_page, registered_user):

        driver =  go_to_registration_page

        driver.find_element(*TestsLocators.LOGIN_LINK_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.RESTORE_PASSWORD_LINK_TEXT))
        driver.find_element(*TestsLocators.RESTORE_PASSWORD_LINK_TEXT).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.REMEMBERED_PASSWORD_LOGIN__LINK_TEXT))
        driver.find_element(*TestsLocators.REMEMBERED_PASSWORD_LOGIN__LINK_TEXT).click()

        email, password = registered_user
        self.login_user(driver, email, password)
        