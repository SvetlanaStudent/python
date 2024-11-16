import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form_submission(driver):
    # Создаем объект страницы
    form_page = FormPage(driver)

    # Открываем страницу
    form_page.open()

    # Заполняем форму
    form_page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        city="Москва",
        country="Россия",
        job="QA",
        company="SkyPro"
    )

    # Нажимаем кнопку Submit
    form_page.submit()

    # Ожидаем появления всех предупреждений
    alerts = form_page.get_alerts()

    # Проверяем, что поле Zip code подсвечено красным
    zip_code_alert = next((alert for alert in alerts if "alert-danger" in alert.get_attribute("class")), None)
    assert zip_code_alert is not None and zip_code_alert.is_displayed(), "Поле Zip code не подсвечено красным."

    # Проверяем, что остальные поля подсвечены зеленым
    for alert in alerts:
        if "alert-right" in alert.get_attribute("class"):
            assert alert.is_displayed(), "Не все поля подсвечены зелёным."