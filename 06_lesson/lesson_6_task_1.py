from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/ajax')
button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton')
button.click()
green_box = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
    )
text = green_box.text
print(text)
driver.quit()
