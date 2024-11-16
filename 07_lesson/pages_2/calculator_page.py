# from selenium.webdriver.common.by import By
#
#
# class CalculatorPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
#
#     def open(self):
#         self.driver.get(self.url)
#
#     def set_delay(self, delay):
#         delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
#         delay_input.clear()
#         delay_input.send_keys(delay)
#
#     def click_button(self, button_text):
#         button = self.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
#         button.click()
#
#     def get_result(self):
#         return self.driver.find_element(By.CSS_SELECTOR, "#result").text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
        button.click()

    def get_result(self):
        return WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )