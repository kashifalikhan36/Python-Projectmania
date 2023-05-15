from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/code_development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(10)
data=driver.find_element('xpath','//*[@id="langSelect-EN"]')
data.click()
data=driver.find_element('xpath','//*[@id="bigCookie"]')
# driver.set_page_load_timeout(1000)
time.sleep(10)
while True:
    data.click()
