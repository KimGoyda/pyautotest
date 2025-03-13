from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self.browser.get(self.url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))  # Поиск элемента

    def click(self, locator):
        self.find(locator).click()  # Клик по элементу

    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)  # Ввод текста в поле

    def open(self, url):
        self.browser.get(url)