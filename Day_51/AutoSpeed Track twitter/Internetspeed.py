from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_driver_path = "C:/code_development/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        self.data=[]
        self.Promised_down='29'
        self.Promised_up='2'
        self.twitter_email='kashifalikhan78677868@gmail.com'
        self.twitter_pass='Password'
        self.twitter_id='Kashifalik360'
        self.get_internet_speed()
        self.twitter_post_text='Hey internet Provider why my internet is Download speed:-{self.data[0]} and Upload Speed:-{self.data[1]}'
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        print("Now i am in speedtest")
        time.sleep(4)
        self.auth=self.driver.find_element('xpath','/html/body/div[5]/div[2]/div/div/div[2]/div[1]/div/button')
        self.auth.click()
        self.go_button=self.driver.find_element('xpath','/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go_button.click()
        time.sleep(60)
        self.down=self.driver.find_element('xpath','/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up=self.driver.find_element('xpath','/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.data.append(self.down)
        self.data.append(self.up)
        print("down:",self.down)
        print("up:",self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(15)
        try:
            self.auth=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a')
            self.auth.click()
            time.sleep(5)
            self.email_input=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            self.email_input.send_keys(self.twitter_email)
            time.sleep(3)
            self.next_button=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
            self.next_button.click()
            time.sleep(3)
            try:
                self.password_input=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                self.password_input.send_keys(self.twitter_pass)
            except:
                self.id=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                self.id.send_keys(self.twitter_id)
                self.next_button=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
                time.sleep(3)
                self.password_input=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                self.password_input.send_keys(self.twitter_pass)
            self.next_button.click()
            self.login_button=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            self.login_button.click()
            print("Twitter Account Logined !")
            time.sleep(5)
            self.post_input=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label')
            self.post_input.send_keys(self.twitter_pass)
            self.post_button=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            self.post_button.click()
            time.sleep(3)
            print('Posted Port:80 Success!')
            self.Auth=self.driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div')
            self.Auth.click()
            time.sleep(400)
        except:
            print("error occours")
            time.sleep(400)