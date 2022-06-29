from telnetlib import EC

import button as button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("https://www.rahulshettyacademy.com/client")
#driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#driver.implicitly_wait("10")
driver.find_element(By.XPATH,"//form/div[1]").send_keys("demo@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2)").send_keys("Satish@1234")
#driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3)").send_keys("Satish@1234")
#button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
button.click()