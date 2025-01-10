from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    """Главная страница"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    catalog_women_clothing = "((// div[@class ='sub-new'])[2] / ul / li)[1]"    # Раздел женской одежды
    catalog_of_clothes_shoes_accessories = "(//ul[@class='sub-1 active']/li)[3]"    # Раздел одежды, обуви и аксессуаров
    name_section = "//h1[@class='cell']"    # Название раздела
    cart = "(//a[@id='w_cart'])[2]"     # Корзина


    # Getters
    def get_catalog_women_clothing(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.catalog_women_clothing)))

    def get_cart(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_catalog_of_clothes_shoes_accessories(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(
            (By.XPATH, self.catalog_of_clothes_shoes_accessories)))

    def get_name_section(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.name_section)))

    # Actions
    def click_catalog_women_clothing(self):
        """Нажимаем на раздел Женской одежды"""
        self.get_catalog_women_clothing().click()
        print("Click catalog women clothing")

    def move_to_catalog_of_clothes_shoes_accessories(self):
        """Наводимся на раздел Одежда, обувь и аксессуары"""
        action = ActionChains(self.driver)
        action.move_to_element(self.get_catalog_of_clothes_shoes_accessories()).perform()
        print("Move to catalog of clothes shoes accessories")

    def click_cart(self):
        """Нажимаем на Корзину"""
        self.get_cart().click()
        print("Click cart")


    # Methods
    """ Выбираем категорию товара"""
    def select_catalog_section(self):
        self.move_to_catalog_of_clothes_shoes_accessories()     # Наводимся на раздел Одежда, обувь и аксессуары
        self.click_catalog_women_clothing()     # Нажимаем на раздел Женской одежды
        self.assert_word(self.get_name_section(), "Женская одежда")     # Проверяем заголовок страницы
