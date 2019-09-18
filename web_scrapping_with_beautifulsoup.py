


import bs4 #for importing beautiful soap library
from urllib.request import urlopen as ureq #for requesting web pages
from bs4 import BeautifulSoup as soup
import csv
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")

#page_soup.body.span
containers = page_soup.findAll("div", {'class':'item-container'})
#len(containers)
file_name = "products1.csv"
f = open(file_name, 'w')
headers = 'brand , product_name , shipping\n'
f.write(headers)
# contain = containers[0]
# container = containers[0]                                                                                                                                                                                                                 
for container in containers:
    #brand_Container = page_soup.find("div",{'class': 'item-info'})  
   
    brand_Container = container.find("a", {"class","item-brand"})
    brands = brand_Container.img['title']
   # brands = container.div.div.a.img['title']
    title_container = container.findAll('a', {'class', 'item-title'})                       
    product_name = title_container[0].text    
    shipping_container = container.findAll('li',{'class', "price-ship"})
    shipping_detail = shipping_container[0].text.strip()
    print(brands)     
    print(product_name) 
    print(shipping_detail)
    product_n =  product_name.replace(',','|')
    list1 = [brands, product_n , shipping_detail ]
    f.write("{} , {} , {} \n".format(brands,product_n, shipping_detail))
f.close()    





