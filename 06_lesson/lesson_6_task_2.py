from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")
blue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Change')]")
blue_button.click()
button_text = blue_button.text
print(f'("{button_text}")')
driver.quit()
