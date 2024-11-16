import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from checkout_page import CheckoutPage

@pytest.fixture
def driver():
    # Запуск Chrome-драйвера с использованием ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_sauce_demo(driver):
    # Шаг 1: Открыть сайт
    driver.get("https://www.saucedemo.com/")

    # Шаг 2: Авторизоваться как стандартный пользователь
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Шаг 3: Добавить в корзину товары
    checkout_page = CheckoutPage(driver)
    checkout_page.add_items_to_cart()

    # Шаг 4: Перейти в корзину
    checkout_page.go_to_cart()

    # Шаг 5: Нажать Checkout
    checkout_page.click_checkout()

    # Шаг 6: Заполнить форму
    checkout_page.fill_checkout_form("Иван", "Иванов", "12345")

    # Шаг 7: Прочитать итоговую стоимость
    total_price = checkout_page.get_total_price()
    total_value = total_price.split("$")[-1]

    # Шаг 8: Проверка, что итоговая сумма равна $58.29
    assert total_value == "58.29", f"Expected total to be $58.29, but got ${total_value}"
    print("Тест пройден успешно!")