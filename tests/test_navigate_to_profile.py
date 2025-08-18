from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestsLocators
from curl import Urls

# Переход в личный кабинет 
class TestNavigationToProfileClickProfileLink:

    # Переход по клику на «Личный кабинет» с главной стрницы на страницу входа в аккаунт, пользователь не залогинен
    def test_navigate_to_profile_when_not_authenticated_logged_in(self, open_site):

        driver = open_site
        
        driver.find_element(*TestsLocators.PERSONAL_ACCOUNT_BUTTON).click()       
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestsLocators.WORKING_AREA_LOGIN))

        assert driver.current_url == Urls.LOGIN_PAGE


    # Переход по клику на «Личный кабинет» с главной стрницы на страницу личного кабинета, пользователь залогинен
    def test_navigate_to_profile_authenticated_logged_in(self, login_user):

        driver = login_user

        driver.find_element(*TestsLocators.PERSONAL_ACCOUNT_BUTTON).click()        
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestsLocators.WORKING_AREA_PROFILE))

        assert driver.current_url == Urls.PROFILE_PAGE
