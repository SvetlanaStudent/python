from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try:
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
    time.sleep(1)
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    print(len(delete_buttons))
finally:
    driver.quit()

