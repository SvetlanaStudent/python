import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера


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
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Шаг 3: Добавить в корзину товары
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

    # Шаг 4: Перейти в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Шаг 5: Нажать Checkout
    driver.find_element(By.ID, "checkout").click()

    # Шаг 6: Заполнить форму
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Шаг 7: Прочитать итоговую стоимость
    total_price = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

    total_text = total_price.text
    total_value = total_text.split("$")[-1]
    
    # Шаг 8: Проверка, что итоговая сумма равна $58.29
    assert total_value == "58.29", f"Expected total to be $58.29, but got ${total_value}"
    print("Тест пройден успешно!")