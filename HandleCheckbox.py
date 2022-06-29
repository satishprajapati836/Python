import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH," //input[@type='checkbox']")
print(len(checkboxes))
for checkboxname in checkboxes:
    if checkboxname.get_attribute("value") == 'option3':
        checkboxname.click()
        break
time.sleep(2)
driver.close()