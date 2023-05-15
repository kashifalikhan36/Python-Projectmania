from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementClickInterceptedException

chrome_driver_path = "C:/code_development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://tinder.com/')
time.sleep(8)
try:
    login_button = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    login_button.click()
    time.sleep(5)
    try:
        login_button = driver.find_element('xpath','/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
        login_button.click()
    except:
        login_button = driver.find_element('xpath','/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/button')
        login_button.click()
        login_button = driver.find_element('xpath','/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
        login_button.click()
    time.sleep(3)
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)
    time.sleep(5)
    user=driver.find_element('xpath','/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
    user.send_keys('kashifalikhan093@gmail.com')
    password=driver.find_element('xpath','/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
    password.send_keys('Aquatype1')
    login=driver.find_element('xpath','/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
    login.click()
    time.sleep(10)
    tinder_window = driver.window_handles[0]
    driver.switch_to.window(tinder_window)
    time.sleep(5)
    auth1=driver.find_element('xpath','/html/body/div[2]/main/div/div/div/div[3]/button[1]')
    auth1.click()
    auth2=driver.find_element('xpath','/html/body/div[2]/main/div/div/div/div[3]/button[2]')
    auth2.click()
    auth3=driver.find_element('xpath','/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
    auth3.click()
    '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button'
    time.sleep(50)
    while True:
        try:
            like=driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
            like.click()
        except ElementClickInterceptedException:
            #Only Back To Tinder Page Left
            like=driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
            like.click()
            continue
except NoSuchElementException:
        print("No application button, skipped.")