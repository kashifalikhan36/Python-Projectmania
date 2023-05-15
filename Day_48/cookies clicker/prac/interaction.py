from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/code_development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.google.co.in/')
data=driver.find_element('xpath','//*[@id="APjFqb"]')
data.send_keys("python")
data.send_keys(Keys.ENTER)