from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
try:
    driver.get('http://the-internet.herokuapp.com/entry_ad')
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='modal']/div[@class='modal-footer']/p[contains(text(), 'Close')]"))
    )
    close_button.click()
finally:
    driver.quit()
