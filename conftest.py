import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import Urls
from locators import TestsLocators
from generator_data import generation_data


# Открывает браузер Chrome, разворачивает окно на максимум, закрывает окно после теста.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Открывает главную страницу сайта 
@pytest.fixture
def open_site(driver):
    driver.get(Urls.MAIN_PAGE)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestsLocators.ENTER_ACCOUNT_BUTTON))
    return driver


# Переход с главной страницы в форму регистрации
@pytest.fixture
def go_to_registration_page(open_site):
    driver = open_site
    driver.find_element(*TestsLocators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestsLocators.REGISTRATION_LINK_TEXT))
    driver.find_element(*TestsLocators.REGISTRATION_LINK_TEXT).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestsLocators.NAME_INPUT))
    return driver
    

# Регистрация нового пользователя, запускается один раз на всю сессию тестирования
@pytest.fixture(scope="session")
def registered_user():
    driver = webdriver.Chrome()
    driver.maximize_window()

    name, email, password = generation_data()

    driver.get(Urls.REGISTRATION_PAGE)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestsLocators.NAME_INPUT))

    driver.find_element(*TestsLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*TestsLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*TestsLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*TestsLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestsLocators.LOGIN_BUTTON))

    driver.quit()

    return email, password


# Авторизациия зарегестированного пользователя
@pytest.fixture
def login_user(open_site, registered_user):
    driver = open_site
    email, password = registered_user

    driver.find_element(*TestsLocators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestsLocators.EMAIL_INPUT))

    driver.find_element(*TestsLocators.EMAIL_INPUT_LOGIN).send_keys(email)      
    driver.find_element(*TestsLocators.PASSWORD_INPUT_LOGIN).send_keys(password)  
    driver.find_element(*TestsLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.ORDER_BUTTON))

    return driver
