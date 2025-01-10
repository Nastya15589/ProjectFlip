import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from base.base_class import Base
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage



# @pytest.mark.order(3)
def test_delete_product(set_up, set_group):
    """Тест удаление товара из корзины"""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    print("Start test 1")

    """ Авторизация """
    login = LoginPage(driver)
    login.authorization()       # Проходим авторизацию

    """ Главная страница """
    mp = MainPage(driver)
    mp.click_cart()     # Переходим в корзину

    """ Корзина """
    cp = CartPage(driver)
    cp.delete_product()     # Удаляем товар из корзины

    """ Скриншот """
    screenshot = Base(driver)
    screenshot.get_screenshot()     # Делаем скриншот

    time.sleep(5)
    print("Finish test 1")
    driver.quit()









