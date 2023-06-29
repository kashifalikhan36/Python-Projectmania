
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementClickInterceptedException

class InstaFollower:
    def __init__(self):
            
        self.chrome_driver_path = "C:/code_development/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        self.username="al_arabiy_always"
        self.password='Password'
        
    def login(self):   
        self.driver.get('https://www.instagram.com')
        time.sleep(8)
        user_input = self.driver.find_element('xpath','/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        user_input.send_keys(self.username)
        password_input = self.driver.find_element('xpath',"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        password_input.send_keys(self.password)
        login_button = self.driver.find_element('xpath','/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
        login_button.click()
        time.sleep(12)

    def find_followers(self):
        self.driver.get('https://www.instagram.com/towardseternity/followers/')
        time.sleep(5)
        
    def follow(self):
        modal = self.driver.find_element('xpath','/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(1,3000000):
            try:
                if i%6==0:
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                    print('scroll')
                    time.sleep(2)
                auth2=self.driver.find_element('xpath',f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button')
                time.sleep(2)
                auth2.click()
            except ElementClickInterceptedException:
                try:
                    time.sleep(2)
                    cancel_button = self.driver.find_element('xath','/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                    cancel_button.click()
                except:
                    print("cancel button not work")
                    time.sleep(6)
            except :
                print('error')
        time.sleep(100)