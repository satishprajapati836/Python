from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("http://the-internet.herokuapp.com/frames")

driver.find_element(By.LINK_TEXT,"iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Satish is able to to Automation Testing")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
#driver.close()