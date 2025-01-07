from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class WomenClothingPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filter_available = "//label[@for='filter-field-i101']"    # Фильтр Доступен
    women_outerwear = "(//a[@class='filter-item main-sections'])[1]"      # Верхняя женская одежда
    left_slider_price = "(//a[@class='ui-slider-handle ui-state-default ui-corner-all'])[1]"    # Левый ползунок Цены
    right_slider_price = "(//a[@class='ui-slider-handle ui-state-default ui-corner-all'])[2]"   # Правый ползунок Цены
    clothing_size_44 = "(//div[@class='filter-label cell'])[13]"  # 44-ый размер одежды
    apply_button_for_slider = "//button[@name='accept-field-change-i205']"  # Кнопка применить для слайдера
    sorting = "//div[@class='active']"  # Сортировка
    sort_by_rating = "//label[contains(text(), 'Рейтингу')]"   # Сортировка по рейтингу
    product = "(//div[@class='new-product'])[1]"    # Продукт

    # Getters
    def get_filter_available(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.filter_available)))

    def get_product(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_sorting(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.sorting)))

    def get_sort_by_rating(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_rating)))

    def get_women_outerwear(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.women_outerwear)))

    def get_left_slider_price(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.left_slider_price)))

    def get_right_slider_price(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.right_slider_price)))

    def get_clothing_size_44(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.clothing_size_44)))

    def get_apply_button_for_slider(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.apply_button_for_slider)))

    # Actions
    def check_filter_available(self):       # Выбрать в фильтре Доступен
        self.get_filter_available().click()
        print("Check filter available")

    def click_women_outerwear(self):        # Выбрать раздел Верхняя женская одежда
        self.get_women_outerwear().click()
        print("Click women outerwear")

    def click_apply_button_for_slider(self):        # Нажать кнопку Применить для слайдера
        self.get_apply_button_for_slider().click()
        print("Click apply button for slider")

    def click_sort_by_rating(self):     # Выбрать сортировку по рейтингу
        self.get_sort_by_rating().click()
        print("Click sort by rating")

    def click_clothing_size_44(self):       # Выбрать размер одежды 44
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.get_clothing_size_44().click()
        print("Click clothing size 44")

    def move_left_slider_price(self):       # Перетащить левый слайдер
        self.driver.execute_script("window.scrollTo(0, 300);")
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_left_slider_price()).move_by_offset(50, 0).release().perform()
        print("Move left slider price")

    def move_right_slider_price(self):      # Перетащить правый слайдер
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_right_slider_price()).move_by_offset(xoffset=-50, yoffset=0).release().perform()
        print("Move right slider price")

    def move_to_sorting(self):      # Навестись на Сортировку
        self.driver.execute_script("window.scrollTo(0, 0);")
        action = ActionChains(self.driver)
        action.move_to_element(self.get_sorting()).perform()
        print("Move to sorting")

    def click_product(self):        # Выбрать продукт
        self.get_product().click()
        print("Select product")

    # Methods
    def select_product(self):
        self.get_current_url()
        self.click_women_outerwear()
        self.click_clothing_size_44()
        self.move_left_slider_price()
        self.move_right_slider_price()
        self.click_apply_button_for_slider()
        self.move_to_sorting()
        self.click_sort_by_rating()
        self.check_filter_available()
        self.click_product()
