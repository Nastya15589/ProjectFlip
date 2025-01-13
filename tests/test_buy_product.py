import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure

from base.base_class import Base
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.place_order_page import PlaceOrder
from pages.product_page import ProductPage
from pages.women_clothing_page import WomenClothingPage


# @pytest.mark.order(3)
@allure.description("Test buy product 1")
def test_buy_product_1(set_up, set_group):
    """Тест покупки товара"""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    print("Start test 1")

    """ Авторизация """
    login = LoginPage(driver)
    login.authorization()       # Проходим авторизацию

    """ Главная страница """
    mp = MainPage(driver)
    mp.select_catalog_section()     # Выбираем раздел в каталоге

    """ Раздел Женской одежды """
    wcp = WomenClothingPage(driver)
    wcp.select_product()        # Выбираем продукт

    """ Страница продукта """
    pp = ProductPage(driver)
    name_brand, name_model, name_product, price_product, size_model = pp.add_product()
    # Получаем производителя, модель, наименование, цену, размер товара и добавляем его в корзину

    """ Корзина """
    cp = CartPage(driver)
    brand_cart, model_cart, name_product_cart, price_cart, product_size_cart = cp.product_information_in_cart()
    # Получаем производителя, модель, наименование, цену, размер товара в корзине

    """ Проверка информации о товаре в корзине """
    check = Base(driver)
    check.assert_word_new(name_model, model_cart)       # Проверяем модель
    check.assert_word_new(name_product, name_product_cart)      # Проверяем наименование товара
    check.assert_word_new(price_product, price_cart)        # Проверяем цену
    check.assert_word_new(size_model, product_size_cart)        # Проверяем размер

    """ Подтверждение заказа """
    cp.product_confirmation()   # Оформляем заказ

    """ Оформление заказа """
    pop = PlaceOrder(driver)
    name_product_in_order, model_and_size_product_in_order = pop.product_information_in_order()
    # Получаем наименование, модель и размер товара в заказе

    """ Проверка информации о товаре в заказе """
    check.assert_word_new(name_product_cart, name_product_in_order)     # Проверяем наименование товара
    check.assert_word_new(f'Название цвета: {model_cart}, Размер: {product_size_cart}',
                          model_and_size_product_in_order)      # Проверяем модель и размер товара

    """ Подтверждение заказа """
    # pop.confirmation_order()      # Подтверждение заказа

    """ Скриншот """
    screenshot = Base(driver)
    screenshot.get_screenshot()       # Делаем скриншот

    time.sleep(5)
    print("Finish test 1")
    driver.quit()









