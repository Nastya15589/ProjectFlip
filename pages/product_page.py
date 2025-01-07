from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    model = "//a[@data-id='0']"    # Выбор модели и расцветки
    size_44 = "(//div[@class='size-color']/label)[1]"    # 44-ый размер
    cart_button = "//input[@id='cart_button']"  # Добавить в корзину
    bread_crumbs = "//div[@class='krohi']/a"        # Хлебные крошки
    brand = "(//div[@class='row clothes-groupped-pack']/div)[2]"        # Производитель
    price = "//div[@class='new-price']"     # Цена товара
    go_to_cart = "//a[@class='gray nbtn float-left']"       # Переход в карзину
    name_product = "//h1"       # Наименование продукта
    available_button = "//a[@id='produce_preorder']"

    # Getters
    def get_select_model(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.model)))

    def get_available_button(self):
        return WebDriverWait(self.driver, 100).until(EC.invisibility_of_element_located((By.XPATH, self.available_button)))

    def get_name_product_and_brand(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_price(self):
        return WebDriverWait(self.driver, 80).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_brand(self):
        return WebDriverWait(self.driver, 80).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    def get_bread_crumbs(self):
        return self.driver.find_elements(By.XPATH, self.bread_crumbs)

    def get_size_44(self):
        return WebDriverWait(self.driver, 80).until(EC.element_to_be_clickable((By.XPATH, self.size_44)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 80).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions
    def click_cart_button(self):        # Добавляем товар в корзину
        self.get_cart_button().click()
        print("Click cart button")

    def click_go_to_cart(self):     # Переходим в корзину
        self.get_go_to_cart().click()
        print("Click go to cart")

    def get_name_model(self):       # Получаем наименование модели товара
        name_model = self.get_select_model().get_attribute("data-value")
        print(f'Название модели: {name_model}')
        return name_model

    def get_name_brand(self):       # Получаем производителя
        name_brand = self.get_brand().text
        print(f'Название производителя: {name_brand}')
        return name_brand

    def get_price_product(self):        # Получаем цену товара
        price_product = self.get_price().text
        print(f'Цена товара: {price_product}')
        return price_product

    def get_size_model(self):       # Получаем размер товара
        size_model = self.get_size_44().text
        print(f'Размер товара: {size_model}')
        return size_model

    def get_name_product(self, name_brand):     # Получаем наименование товара
        name_product = self.get_name_product_and_brand().text.replace(name_brand + " ", "")
        print(f'Название продукта: {name_product}')
        return name_product

    def select_size(self):      # Выбираем 44-ый размер товара
        self.get_size_44().click()
        print("Select size")

    def get_list_bread_crumbs(self):        # Получаем хлебные крошки
        elements = list(self.get_bread_crumbs())
        element = [i.get_attribute("title") for i in elements]
        print(element)

    # Methods
    def add_product(self):
        self.get_current_url()
        self.get_list_bread_crumbs()
        name_brand = self.get_name_brand()
        name_model = self.get_name_model()
        name_product = self.get_name_product(name_brand)
        self.select_size()
        try:
            self.get_available_button()
        except:
            print("Данного товара нет")
            for i in range(4):
                size_44 = f"(//div[@class='size-color']/label)[{i+1}]"
                self.get_size_model()
                if self.get_available_button():
                    break
                else:
                    continue

        else:
            size_model = self.get_size_model()
            price_product = self.get_price_product()
            self.click_cart_button()

            self.click_go_to_cart()
            return name_brand, name_model, name_product, price_product, size_model