import datetime


class Base:
    """Общие методы"""
    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        """Получаем текущий URL"""
        get_url = self.driver.current_url
        print("Current url " + get_url)


    def assert_word(self, word, result):
        """Проверяем текст"""
        value_word = word.text
        assert value_word == result
        print("Good value word")


    def assert_word_new(self, word, result):
        assert word == result
        print("Good value word")


    def get_screenshot(self):
        """Делаем скриншот экрана"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(".\\ProjectFlip\\screen\\" + name_screenshot)
        print("Скриншот выполнен")


    def assert_url(self, result):
        """Проверяем URL"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")
