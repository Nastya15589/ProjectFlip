import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from base.base_class import Base
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.place_order_page import PlaceOrder
from pages.product_page import ProductPage
from pages.women_clothing_page import WomenClothingPage


# @pytest.mark.order(3)
def test_delete_product(set_up, set_group):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    print("Start test 1")

    """ Авторизация """
    login = LoginPage(driver)
    login.authorization()

    """ Главная страница """
    mp = MainPage(driver)
    mp.click_cart()

    """ Корзина """
    cp = CartPage(driver)
    cp.delete_product()

    """ Скриншот """
    # screenshot = Base(driver)
    # screenshot.get_screenshot()

    time.sleep(10)
    print("Finish test 1")
    driver.quit()









