from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

dropdpwn = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdpwn.select_by_index(1)
dropdpwn.select_by_visible_text("Female")