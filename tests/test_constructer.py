#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestsLocators

# Навигация по секциям раздела «Конструктор» на главной странице
class TestNavigateSectionConstructer:

    # Переход к разделу "Начинки"
    def test_navigate_constructer_from_main_page_to_fillings(self, open_site):

        driver = open_site

        driver.find_element(*TestsLocators.FILLINGS_TAB_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.FILLINGS_SECTION_TITLE))
                                       
        assert driver.find_element(*TestsLocators.FILLINGS_SECTION_TITLE).is_displayed()


    # Переход к разделу "Соусы"
    def test_navigate_constructer_from_main_page_to_sauces(self, open_site):

        driver = open_site

        driver.find_element(*TestsLocators.SAUCES_TAB_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.SAUCES_SECTION_TITLE))

        assert driver.find_element(*TestsLocators.SAUCES_SECTION_TITLE).is_displayed()


    # Переход к разделу "Булки"
    def test_navigate_constructer_from_main_page_to_buns(self, open_site):

        driver = open_site

        driver.find_element(*TestsLocators.FILLINGS_TAB_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.FILLINGS_SECTION_TITLE))
        driver.find_element(*TestsLocators.BUNS_TAB_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.BUNS_SECTION_TITLE))

        assert driver.find_element(*TestsLocators.BUNS_SECTION_TITLE).is_displayed()
        