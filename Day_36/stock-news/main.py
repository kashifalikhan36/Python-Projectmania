#api key is now paid now so this project are also gonna cancel today

import requests
import datetime
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

APIKEY="1CMO778072IY80RI"

NEWS_APIKEY="c5cc28b4fc4d438bb748b26f871b87aa"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today_date=str(datetime.datetime.now().date())
today = datetime.date.today() - datetime.timedelta(days=2)
# today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
reponse_news=requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={NEWS_APIKEY}")


print(reponse_news.json())
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

