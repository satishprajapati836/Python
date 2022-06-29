import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radiobuttons = driver.find_elements(By.XPATH,"//input[@name='radioButton']")
for radio in radiobuttons:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()
        break
assert driver.find_element(By.XPATH,"//input[@id='displayed-text']").is_displayed()
driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()
assert driver.find_element(By.XPATH,"//input[@id='displayed-text']").is_displayed()