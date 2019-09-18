# import requests
# from bs4 import BeautifulSoup

# URL = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Digital-Camera/dp/B07WHJN2CC/ref=sr_1_2?keywords=sony+A7&qid=1568473674&s=gateway&sr=8-2'
# headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

# page = requests.get(URL, headers = headers) 
# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify())
# title = soup.findAll('div', {id: 'titleSection'})
# print(title)

import bs4 #for importing beautiful soap library
from urllib.request import urlopen as ureq #for requesting web pages
from bs4 import BeautifulSoup as soup
import csv
import smtplib
my_url = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Digital-Camera/dp/B07WHJN2CC/ref=sr_1_2?keywords=sony+A7&qid=1568473674&s=gateway&sr=8-2'

def check_price():
    uclient = ureq(my_url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find(id='productTitle').get_text()
    price = page_soup.find(id='priceblock_ourprice').get_text()
    print(containers.strip())
    print(price.strip())
    converted_price = price.replace(',', '')
    converted_price1 = float(converted_price[1:6])
    print(converted_price1)
    if(converted_price1 < 1700.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('shehzadbaloch984@gmail.com', 'jacksparow12')
    subject = 'Alert message from Amazon'
    body = 'Hurrah : price fell down fell free to shop  Check the amazon link https://www.amazon.com/Sony-Full-Frame-Mirrorless-Digital-Camera/dp/B07WHJN2CC/ref=sr_1_2?keywords=sony+A7&qid=1568473674&s=gateway&sr=8-2'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'shehzadbaloch984@gmail.com',
        'shehzadmunir986@gmail.com',
        msg
    )
    print('Hey email been sent')
    server.quit()

check_price()    

