from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

#  driver.find_element(By.XPATH,"//input[@class = 'form-control ng-pristine ng-invalid ng-touched']").send_keys("Satish")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Satish")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("satish@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Satish@1234")
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").submit()
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("Satish QA")
Message = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(Message)
assert 'success' in Message
#driver.close()