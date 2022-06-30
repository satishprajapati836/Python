from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")