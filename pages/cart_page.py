from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):
    """Страница корзина"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    title_page = "//h1"     # Заголовок страницы
    name_product_cart = "//b/a"     # Наименование товара в корзине
    name_model_cart = "(//div[@class='caddi txt_gray'])[1]"     # Наименование модели товара в корзине
    product_size_cart = "(//div[@class='caddi txt_gray'])[2]"       # Размер товара в корзине
    brand_cart = "(//div[@class='cadd txt_gray'])[2]"       # Наименование производителя товара в корзине
    model_cart = "(//div[@class='caddi txt_gray'])[2]"      # Наименование модели товара в корзине
    price_cart = "(//b[@class='no-br'])[1]"         # Цена товара в корзине
    checkbox = "(//input[@name='selected[]'])[1]"       # Чекбокс по выбору товара
    submit_button = "(//input[@type='submit'])[1]"      # Кнопка оформления заказа
    delete_button = "//a[@class='nbtn gray small m-r-10']"     # Удалить товар
    empty_cart_message = "//p[contains(text(), 'В Вашей корзине пусто :(')]"    # Сообщение о пустой корзине


    # Getters
    def get_title_page(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.title_page)))

    def get_empty_cart_message(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart_message)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_delete_product(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.delete_button)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_price(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.price_cart)))

    def get_brand(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.brand_cart)))

    def get_model(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.model_cart)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.name_product_cart)))

    def get_name_model(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.name_model_cart)))

    def get_product_size(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.product_size_cart)))


    # Actions
    def get_name_model_cart(self):
        """Получаем Наименование модели товара в корзине"""
        name_model_cart = self.get_name_model().text.split(": ")[1]
        print(f'Название модели в корзине:{name_model_cart}')
        return name_model_cart

    def get_brand_cart(self):
        """Получаем Производителя товара в корзине"""
        brand_cart = self.get_brand().text.split(": ")[1]
        print(f'Производитель товара в корзине:{brand_cart}')
        return brand_cart

    def get_name_product_cart(self):
        """Получаем Наименование товара в корзине"""
        name_product_cart = self.get_name_product().text
        print(f'Наименование товара в корзине:{name_product_cart}')
        return name_product_cart

    def get_product_size_cart(self):
        """Получаем Размер товара в корзине"""
        product_size_cart = self.get_product_size().text.split(": ")[1]
        print(f'Размер товара в корзине:{product_size_cart}')
        return product_size_cart

    def get_price_cart(self):
        """Получаем Цену товара в корзине"""
        price_cart = self.get_price().text
        print(f'Цена товара в корзине:{price_cart}')
        return price_cart

    def click_submit_button(self):
        """Нажимаем на кнопку оформления заказа"""
        self.get_submit_button().click()
        print("Click submit button")

    def check_checkbox(self):
        """Нажали на чекбокс"""
        self.get_checkbox().click()
        print("Check checkbox")

    def click_delete_product(self):
        """Нажимаем на кнопку удалить"""
        self.get_delete_product().click()
        print("click delete product")


    # Method
    """ Информация о товаре в корзине """
    def product_information_in_cart(self):
        self.get_current_url()      # Получаем текущую url
        self.assert_word(self.get_title_page(), "Корзина")      # Проверяем заголовок страницы
        name_product_cart = self.get_name_product_cart()        # Получаем наименование товара
        brand_cart = self.get_brand_cart().title()      # Получаем производителя товара
        model_cart = self.get_name_model_cart()     # Получаем модель товара
        product_size_cart = self.get_product_size_cart()        # Получаем размер товара
        price_cart = self.get_price_cart()      # Получаем цену товара
        return brand_cart, model_cart, name_product_cart, price_cart, product_size_cart


    """ Подтверждение оформления заказа """
    def product_confirmation(self):
        self.click_submit_button()


    """ Удаление товара из корзины """
    def delete_product(self):
        self.get_current_url()      # Получаем текущую url
        self.assert_word(self.get_title_page(), "Корзина")      # Проверяем заголовок страницы
        self.click_delete_product()     # Удаляем товар
        self.assert_word(self.get_empty_cart_message(), "В Вашей корзине пусто :(")     # Проверяем сообщение
