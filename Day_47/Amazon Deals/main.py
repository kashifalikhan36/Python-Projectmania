import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "itnajitna@gmail.com"
passw = "password"

account_sid ="sid"
auth_token ="token"

Product_URL="https://www.amazon.in/gp/product/B0BQC1L5XW/ref=ox_sc_act_title_1?smid=A2GTG1HPYW8M2P&psc=1"
HEADER={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8"
}
response=requests.get(url=Product_URL,headers=HEADER).text
soup=BeautifulSoup(response,"lxml")
price=int(soup.find("span",class_="a-price-whole").text.strip("."))
title=soup.find("span", id="productTitle", class_="a-size-large product-title-word-break")

if price<700:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=passw)
        connection.sendmail(
        from_addr=my_email,
        to_addrs="Kashifalikhan093@gmail.com",
        msg=f"Subject:Ur Amazon Deal !!! \nOnly rs:{price} to get {title}".encode('utf-8')
    )