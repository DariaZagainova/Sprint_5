from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestsLocators


# Функция авторизует пользователя по email-паролю. Используется в тестах класса TestLoginFromDifferentPages в файле test_login.py.
def login_user(driver, email, password):

    driver.find_element(*TestsLocators.EMAIL_INPUT_LOGIN).send_keys(email)      
    driver.find_element(*TestsLocators.PASSWORD_INPUT_LOGIN).send_keys(password)  
    driver.find_element(*TestsLocators.LOGIN_BUTTON).click()   
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestsLocators.ORDER_BUTTON))
