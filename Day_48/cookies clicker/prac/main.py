from selenium import webdriver

chrome_driver_path = "C:/code_development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.python.org/")
data={}
for i in range(0,5):
    index_no=i
    i+=1
    time=driver.find_element("xpath", f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time').text
    name=driver.find_element("xpath", f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text
    data[index_no]={'time':time,'name':name}
print(data)

