import requests
from bs4 import BeautifulSoup

def mobile(max_pages):
  page=2
  while page<=max_pages:
    url='https://www.mysmartprice.com/mobile/pricelist/pages/samsung-mobile-price-list-in-india-'+str(page)+'.html' 
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,'lxml')
    for link in soup.findAll('a',{'class':'prdct-item__name'}):
      href=link.get('href')
      title=link.string
      get_s_d(href)
      #print(href)
      #print(title)
    page=page+1

def get_s_d(it_url):
    source_code=requests.get(it_url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text)
    for it_name in soup.findAll('li'):
      print(it_name.string)



mobile(8)
    
