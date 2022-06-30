import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@name='name']").click()
action = ActionChains(driver)
action.key_down(Keys.SHIFT).send_keys('satish').perform()
action.context_click(driver.find_element(By.XPATH,"//input[@name='name']")).perform()