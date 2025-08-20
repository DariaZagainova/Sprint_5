from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestsLocators
from curl import Urls

# Переход из личного кабинета в конструктор 
class TestNavigationFromProfile:

    # По клику на «Конструктор»
    def test_navigate_from_profile_click_button_constructor_go_main_page(self, login_user):

        driver = login_user

        driver.find_element(*TestsLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestsLocators.CONSTRUCTOR_BUTTON))
        driver.find_element(*TestsLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestsLocators.WORKING_AREA_MAIN_PAGE))
                                       
        assert driver.current_url == Urls.MAIN_PAGE


    # По клику на логотип Stellar Burgers
    def test_navigate_from_profile_click_logo_go_main_page(self, login_user):

        driver = login_user

        driver.find_element(*TestsLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestsLocators.LOGO_STELLAR_BURGERS))
        driver.find_element(*TestsLocators.LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestsLocators.WORKING_AREA_MAIN_PAGE))
                                       
        assert driver.current_url == Urls.MAIN_PAGE
