Задание 28.1

Тестирование сервиса https://b2c.passport.rt.ru согласно требованиям: https://docs.google.com/document/d/1qr0cClFsVlUkiXQ-R6SSgere7oU4h7ft/edit?usp=sharing&ouid=107126184225423339882&rtpof=true&sd=true

Описание тест-кейсов и баг-репорты https://docs.google.com/spreadsheets/d/1mdb72amxt8ZikC7lJWNW8BzyVExPR74EXhBZlNYJIFw/edit?usp=sharing (проверено через режим инкогнито, открывается)

Для написания тест-кейсов использовались техники тест-дизайна:

Классы эквивалентности

Граничных значений



data_basic.py - базовые классы, процедуры, функции и локаторы для автотестов

settings.py - регистрационные данные для позитивных тестов авторизации

RST_tests.py - набор автотестов. нумерация соответствует номеру тест-кейса в документе

Драйвер лежит в одной папке с тест-скриптом для запуска автотестов

python -m pytest -v --driver Chrome --driver-path chromedriver.exe RST_tests.py