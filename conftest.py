import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")  # Размер окна
    driver = webdriver.Chrome( options=options)  # Инициализация драйвера
    yield driver  # Передача драйвера в тест
    driver.quit()  # Закрытие браузера после теста
