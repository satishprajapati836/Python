import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Satish")
driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
time.sleep(5)
alertbox = driver.switch_to.alert
alertbox.text
print(alertbox.text)
#alertbox.accept()
alertbox.dismiss()