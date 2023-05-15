from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from selenium.common.exceptions import ElementClickInterceptedException
class RentResearch():
    def __init__(self):
        self.prices=[]
        self.links=[]
        self.address=[]
        pass
    def get_data(self):
        self.Product_URL="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
        HEADER={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
            "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8"
        }
        response=requests.get(url=self.Product_URL,headers=HEADER).text
        soup=BeautifulSoup(response,"lxml")
        element = soup.find_all('span', {'data-test': 'property-card-price'})
        for i in element:
            self.prices.append(i.text)
        element = soup.find_all('address', {'data-test': 'property-card-addr'})
        for i in element:
            self.address.append(i.text)
        element = soup.find_all('a', {'data-test': 'property-card-link'})
        for i in element:
            self.links.append("https://www.zillow.com/"+i['href'])
    def execute(self):
        self.chrome_driver_path = "C:/code_development/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver_path) 
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLScCcSA2ikTm2d1SO5BcfcwANvSePR_rFbvqTdXXHk0Vz59zSA/viewform?usp=sf_link')
        time.sleep(2)
        temp=0
        for i in self.prices:
            time.sleep(2)
            self.form_fill(self.address[temp],self.prices[temp],self.links[temp])
            temp+=1
    def form_fill(self,address,price,link):
        self.data=self.driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.data.send_keys(address)
        self.data=self.driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.data.send_keys(price)
        self.data=self.driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.data.send_keys(link)
        self.data=self.driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        self.data.click()
        time.sleep(1)
        self.data=self.driver.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        self.data.click()
        time.sleep(1)