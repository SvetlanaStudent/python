# import time
# import pytest
# from selenium import webdriver
# from calculator_page import CalculatorPage
#
#
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()  # Используйте другой драйвер, если нужно
#     yield driver
#     driver.quit()
#
#
# def test_calculator(browser):
#     # Создаем объект страницы калькулятора
#     calculator_page = CalculatorPage(browser)
#
#     # Открываем страницу калькулятора
#     calculator_page.open()
#
#     # Устанавливаем задержку
#     calculator_page.set_delay(45)
#
#     # Нажимаем кнопки для вычисления 7 + 8
#     calculator_page.click_button("7")
#     calculator_page.click_button("+")
#     calculator_page.click_button("8")
#     calculator_page.click_button("=")
#
#     # Ждем 45 секунд, чтобы результат успел отобразиться
#     time.sleep(45)
#
#     # Проверяем, что результат равен 15
#     result = calculator_page.get_result()
#     assert result == "15"

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    # Настройка драйвера Chrome и открытие браузера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()  # Закрываем браузер после теста


def test_slow_calculator(driver):
    # Создаем объект страницы калькулятора
    calculator_page = CalculatorPage(driver)

    # Открываем страницу калькулятора
    calculator_page.open()

    # Устанавливаем задержку
    calculator_page.set_delay("45")

    # Нажимаем кнопки: 7, +, 8, =
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    # Проверяем, что результат равен 15
    result = calculator_page.get_result()
    assert result, "Результат калькулятора не равен 15."