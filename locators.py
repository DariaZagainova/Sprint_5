from selenium.webdriver.common.by import By

class TestsLocators:

    # Главная страница
    WORKING_AREA_MAIN_PAGE = (By.CLASS_NAME, "App_componentContainer__2JC2W") #Рабочая область главной страницы
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка 'Войти в аккаунт'/если пользователь не залогинен
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка 'Оформить заказ'/ если пользователь залогинен
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']") # Кнопка 'Личный кабинет'

    # Раздел "Конструктор"
    FILLINGS_TAB_BUTTON = (By.XPATH, "//span[text()='Начинки']") # Кнопка вкладки "Начинки"
    FILLINGS_SECTION_TITLE = (By.XPATH, "//h2[text()='Начинки']") # Заголовок "Начинки" в меню начинок
    SAUCES_TAB_BUTTON = (By.XPATH, "//span[text()='Соусы']") # Кнопка вкладки "Соусы"
    SAUCES_SECTION_TITLE = (By.XPATH, "//h2[text()='Соусы']") # Заголовок "Соусы" в меню соусов
    BUNS_TAB_BUTTON = (By.XPATH, "//span[text()='Булки']") # Кнопка вкладки "Булки"
    BUNS_SECTION_TITLE = (By.XPATH, "//h2[text()='Булки']") # Заголовок "Булки" в меню булок


    # Страница входа в аккаунт
    WORKING_AREA_LOGIN = (By.CLASS_NAME, "Auth_login__3hAey") # Рабочая область страницы входа в аккаунт
    EMAIL_INPUT_LOGIN = (By.XPATH, "//label[text()='Email']/..//input") # Поле ввода логина = email
    PASSWORD_INPUT_LOGIN = (By.NAME, 'Пароль') # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка 'Войти'
    REGISTRATION_LINK_TEXT = (By.LINK_TEXT, "Зарегистрироваться") # Ссылка на переход к странице регистрации 'Зарегистрироваться'
    RESTORE_PASSWORD_LINK_TEXT = (By.XPATH, "//a[text()='Восстановить пароль']") # Ссылка на переход к странице восстановления пароля 'Восстановить пароль'

    # Cтраница регистрации   
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/..//input") # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/..//input") # Поле ввода логина = email
    PASSWORD_INPUT = (By.NAME, 'Пароль') # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка 'Зарегистрироваться'
    ERROR_PASSWORD_TEXT = (By.XPATH, "//p[text()='Некорректный пароль']") # Надпись 'Некорректный пароль'
    LOGIN_LINK_ON_REGISTRATION_PAGE = (By.XPATH, "//a[text()='Войти']") # Ссылка на переход к странице входа в аккаунт 'Войти'

    # Страница восстановления пароля
    REMEMBERED_PASSWORD_LOGIN__LINK_TEXT = (By.XPATH, "//a[text()='Войти']") # Ссылка на переход к странице входа в аккаунт 'Войти'

    # Страница личного кабинета
    WORKING_AREA_PROFILE = (By.CLASS_NAME, "Modal_modal__P3_V5") # Рабочая область личного кабинета
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка 'Конструктор''
    LOGO_STELLAR_BURGERS = (By.CLASS_NAME,"AppHeader_header__logo__2D0X2") # Логотип Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка выйти
