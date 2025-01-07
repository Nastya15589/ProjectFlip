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
def test_buy_product_1(set_up, set_group):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    print("Start test 1")

    """ Авторизация """
    login = LoginPage(driver)
    login.authorization()

    """ Главная страница """
    mp = MainPage(driver)
    mp.select_catalog_section()

    """ Раздел Женской одежды """
    wcp = WomenClothingPage(driver)
    wcp.select_product()

    """ Страница продукта """
    pp = ProductPage(driver)
    name_brand, name_model, name_product, price_product, size_model = pp.add_product()

    """ Корзина """
    cp = CartPage(driver)
    brand_cart, model_cart, name_product_cart, price_cart, product_size_cart = cp.product_information_in_cart()

    """ Проверка информации о товаре в корзине """
    check = Base(driver)
    check.assert_word_new(name_brand, brand_cart)
    check.assert_word_new(name_model, model_cart)
    check.assert_word_new(name_product, name_product_cart)
    check.assert_word_new(price_product, price_cart)
    check.assert_word_new(size_model, product_size_cart)

    """ Подтверждение заказа """
    cp.product_confirmation()

    """ Оформление заказа """
    pop = PlaceOrder(driver)
    name_product_in_order, model_and_size_product_in_order = pop.product_information_in_order()

    """ Проверка информации о товаре в заказе """
    check.assert_word_new(name_product_cart, name_product_in_order)
    check.assert_word_new(f'Название цвета: {model_cart}, Размер: {product_size_cart}', model_and_size_product_in_order)

    """ Подтверждение заказа """
    # pop.confirmation_order()

    """ Скриншот """
    # screenshot = Base(driver)
    # screenshot.get_screenshot()

    time.sleep(10)
    print("Finish test 1")
    driver.quit()








