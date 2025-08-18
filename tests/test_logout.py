from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestsLocators
from curl import Urls

# Выход из аккаунта
class TestLogout:

    # Выход по кнопке «Выйти» в личном кабинете.
    def test_logout_user(self, login_user):

        driver = login_user

        driver.find_element(*TestsLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.LOGOUT_BUTTON))
        driver.find_element(*TestsLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestsLocators.WORKING_AREA_LOGIN))
                                       
        assert driver.current_url == Urls.LOGIN_PAGE
