from selenium import webdriver
chrome_driver_path = "C:/Development/chromedriver"

driver = webdriver.Chrome()

driver.get("https://www.amazon.com")

driver.close()
driver.quit()