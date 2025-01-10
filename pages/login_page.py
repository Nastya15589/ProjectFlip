from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    """Страница авторизации"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    url = 'https://www.flip.kz/'

    # Locators
    mail = "//input[@id='username-pass']"   # Войти через почту
    password = "//input[@id='password']"
    enter_with_password = "//a[contains(text(), 'Войти используя пароль')]"     # Войти используя пароль
    input_link = "//a[@class='p500']"
    input_button = "(//input[@class='nbtn yellow'][@type='submit'])[3]"     # Кнопка Войти
    account = "//a[contains(text(), 'Анастасия')]"      # Аккаунт пользователя


    # Getters
    def get_input_link(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.input_link)))

    def get_enter_with_password(self):
        return WebDriverWait(self.driver, 70).until(EC.element_to_be_clickable((By.XPATH, self.enter_with_password)))

    def get_mail(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_input_button(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.input_button)))

    def get_account(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.account)))


    # Actions
    def click_input_link(self):
        """Нажимаем на Войти"""
        self.get_input_link().click()
        print("Click Input")

    def click_enter_with_password(self):
        """Нажимаем на Войти с помощью пароля"""
        self.get_enter_with_password().click()
        print("Click enter with password")

    def input_mail(self):
        """Вводим почту"""
        self.get_mail().send_keys("n54441863@gmail.com")
        print("Input mail")

    def input_password(self):
        """Вводим пароль"""
        self.get_password().send_keys("n~9dQkYc8e=d~3P")
        print("Input password")

    def click_input_button(self):
        """Нажимаем на кнопку войти"""
        self.get_input_button().click()
        print("Click Input button")


    # Method
    """ Authorization """
    def authorization(self):
        self.driver.get(self.url)       # Открываем страницу
        self.driver.maximize_window()       # Раскрываем окно браузера полностью
        self.get_current_url()      # Получаем текущую url
        self.click_input_link()     # Нажимаем на кнопку Войти
        self.click_enter_with_password()        # Нажимаем на кнопку Войти с паролем
        self.input_mail()       # Вводим почту
        self.input_password()       # Вводим пароль
        self.click_input_button()       # Нажимаем на кнопку Войти
        self.assert_word(self.get_account(), 'Анастасия')       # Проверяем аккаунт пользователя
