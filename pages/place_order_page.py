from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PlaceOrder(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    confirm_button = "//input[@class='confirm-order']"      # Кнопка подтвердить заказ
    name_product_in_order = "(//div[@class='cell p-l-8']/div)[1]"       # Наименование товара в заказе
    model_and_size_product = "(//div[@class='gray small p-t-4'])[1]"        # Наименование модели и размера товара в заказе

    # Getters
    def get_confirm_button(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.name_product_in_order)))

    def get_model_and_size_product(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.model_and_size_product)))

    # Actions
    def click_confirm_button(self):     # Нажимаем на Кнопку подтвердить заказ
        self.get_confirm_button().click()
        print("Click confirm button")

    def get_name_product_in_order(self):        # Получаем Наименование товара в заказе
        name_product_in_order = self.get_name_product().text
        print(f'Наименование товара в заказе: {name_product_in_order}')
        return name_product_in_order

    def get_model_and_size_product_in_order(self):      # Получаем Наименование модели и размера товара в заказе
        model_and_size_product_in_order = self.get_model_and_size_product().text
        print(f'Модель и размер товара в заказе: {model_and_size_product_in_order}')
        return model_and_size_product_in_order

    # Method
    def product_information_in_order(self):
        self.get_current_url()
        self.assert_url("https://www.flip.kz/order?form=preview")
        name_product_in_order = self.get_name_product_in_order()
        model_and_size_product_in_order = self.get_model_and_size_product_in_order()
        return name_product_in_order, model_and_size_product_in_order

    def confirmation_order(self):
        self.click_confirm_button()
