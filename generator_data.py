import random

# фунцкия генерация логина / логин = email
def generation_data():
    
    first_name = 'Daria'
    last_name = 'Zagainova'
    cohort = '28FS'
    random_digits = random.randint(100, 999)
    domain = 'yandex.ru'

    name = 'Daria'
    email = f'{first_name}{last_name}_{cohort}_{random_digits}@{domain}'
    password = 'practicum'

    return name, email, password
