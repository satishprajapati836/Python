from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/#/practice-project")
print(driver.title)
print(driver.current_url)
driver.get("https://www.google.com/")
#driver.minimize_window()
print(driver.title)
driver.back()
driver.forward()
#driver.refresh()
#driver.close()