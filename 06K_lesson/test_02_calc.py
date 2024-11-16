import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Настройка драйвера Chrome и открытие браузера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()  # Закрываем браузер после теста

def test_slow_calculator(driver):
    # Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввести значение 45 в поле #delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()  # Очистить поле перед вводом
    delay_input.send_keys("45")

    # Нажать на кнопки: 7, +, 8, =
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(1)").click()  # Кнопка 7
    driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()  # Кнопка +
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(2)").click()  # Кнопка 8
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()  # Кнопка =


    # Ожидать результата 15 в поле результата
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Проверка результата
    assert result, "Результат калькулятора не равен 15."
