# python -m pytest -v --driver Chrome --driver-path chromedriver.exe RST_tests.py


from time import sleep
from data_basic import *
from settings import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


### RS_2 - общий вид формы (сохраняется скриншот)
def test_002_vision(selenium):
    form = AuthForm(selenium)
    form.driver.save_screenshot('screen_001.jpg')


### RS_5 - тест, что по-умолчанию выбрана форма авторизации по телефону
def test_005_by_phone(selenium):
    form = AuthForm(selenium)

    assert form.placeholder.text == 'Мобильный телефон'


### RS_6 - тест автосмены "таб ввода"
def test_006_change_placeholder(selenium):
    form = AuthForm(selenium)

    # ввод номера телефона
    form.username.send_keys('+79637718323')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Мобильный телефон'

    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод почты
    form.username.send_keys('kitty@mail.bk')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Электронная почта'

    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод логина
    form.username.send_keys('MyLogin')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Логин'


### RS_7 - позитивный сценарий авторизации по телефону
def test_007_positive_by_phone(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'


### RS_8 - негативный сценарий авторизации по телефону
def test_007_negative_by_phone(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys('+79435823517')
    form.password.send_keys('randompass')
    sleep(5)
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'


### RS_9 - позитивный сценарий авторизации по почте
def test_009_positive_by_email(selenium):
    form = AuthForm(selenium)

    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'


### RS_10 -  негативный сценарий авторизации по почте
def test_010_negative_by_email(selenium):
    form = AuthForm(selenium)

    # ввод почты
    form.username.send_keys('kitty@gmail.com')
    form.password.send_keys('randompass')
    sleep(5)
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'


### RS_16 - получение временного кода на телефон и открытие формы для ввода кода
def test_016_get_code(selenium):
    form = CodeForm(selenium)

    # ввод телефона
    form.address.send_keys(valid_phone)

    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(30)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code


### RS_20 - переход в форму восстановления пароля, открытие формы
def test_020_forgot_pass(selenium):
    form = AuthForm(selenium)

    # клик по надписи "Забыл пароль"
    form.forgot.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Восстановление пароля'


### RS_21 - переход в форму регистрации, открытие формы
def test_021_register(selenium):
    form = AuthForm(selenium)

    # клик по надписи "Зарегистрироваться"
    form.register.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Регистрация'


### RS_22 - проверка открытия пользовательского соглашения
def test_022_agreement(selenium):
    form = AuthForm(selenium)

    original_window = form.driver.current_window_handle
    # клик по надписи "Пользовательским соглашением" в подвале страницы
    form.agree.click()
    sleep(5)
    WebDriverWait(form.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in form.driver.window_handles:
        if window_handle != original_window:
            form.driver.switch_to.window(window_handle)
            break
    win_title = form.driver.execute_script("return window.document.title")

    assert win_title == 'User agreement'


### RS_23 - переход по ссылке авторизации через вконтакте
def test_023_auth_vk(selenium):
    form = AuthForm(selenium)
    form.vk_btn.click()
    sleep(5)

    assert form.get_base_url() == 'oauth.vk.com'


### RS_24 - переход по ссылке авторизации через одноклассники
def test_024_auth_ok(selenium):
    form = AuthForm(selenium)
    form.ok_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.ok.ru'


### RS_25 - переход по ссылке авторизации через майлру
def test_025_auth_mailru(selenium):
    form = AuthForm(selenium)
    form.mailru_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.mail.ru'


### RS_26 - переход по ссылке авторизации через google
def test_026_auth_google(selenium):
    form = AuthForm(selenium)
    form.google_btn.click()
    sleep(5)

    assert form.get_base_url() == 'accounts.google.com'


### RS_27 - переход по ссылке авторизации через яндекс
def test_027_auth_ya(selenium):
    form = AuthForm(selenium)
    form.ya_btn.click()
    sleep(5)

    assert form.get_base_url() == 'passport.yandex.ru'