#! /usr/local/bin/python3.8

# Задание к модулю 1.3
# Необходимо спарсить данные о вакансиях python разработчиков с сайта hh.ru, введя в поиск “python разработчик” и указав, что мы рассматриваем все регионы. Необходимо спарсить:
# Название вакансии
# Требуемый опыт работы
# Заработную плату
# Регион
                

import requests
import json
import time
from bs4 import BeautifulSoup
data={
      "data":[]
      }

req = requests.Session()
get_header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:104.0) Gecko/20100101 Firefox/104.0', 'Host' : 'hh.ru'}
url='https://hh.ru/'
resp = req.get(url, headers=get_header, allow_redirects=False)
url = resp.headers['location']
get_header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:104.0) Gecko/20100101 Firefox/104.0', 'Host' : url[8:-1]}
resp = req.get(url, headers=get_header, allow_redirects=False)
url='https://spb.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50'
resp = req.get(url, headers=get_header, allow_redirects=False)
soup=BeautifulSoup(resp.text, "lxml")
next_page_url = soup.find(attrs={'class':"bloko-button", "data-qa":"pager-next"}).attrs['href']
while next_page_url:
    items_list=soup.find_all(attrs={"class":"vacancy-serp-item-body"})
    for item in items_list:
        item_url = item.find(attrs={"class":"serp-item__title"})['href']
        item_title = item.find(attrs={"class":"serp-item__title"}).text
        try:
            item_SS = item.find(attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text
        except:
            item_SS = ""
        item_address = item.find(attrs={"data-qa":"vacancy-serp__vacancy-address"}).text
        resp_vacantion = req.get(item_url, headers=get_header, allow_redirects=False)
        soup_vacantion=BeautifulSoup(resp_vacantion.text, "lxml")
        try:
            item_experience=soup_vacantion.find(attrs={"class":"vacancy-description-list-item"}).text
        except:
            item_experience=""
#        print(item)
#        print(item_url,item_title,item_SS,item_address)
        data['data'].append({"title":item_title, "work experience":item_experience, "salary":item_SS, "region":item_address})
        print(data)
        #print (item_soup.find(attrs={"class":"serp-item__title"}).text)
    url="https://spb.hh.ru"+next_page_url
    with open('data.json','w') as file:
        json.dump(data,file)
    
#    exit()

    print("loading next page ...", end=' ')
    resp = req.get(url, headers=get_header, allow_redirects=False)
    print ("ok")
    time.sleep(20)
    soup=BeautifulSoup(resp.text, "lxml")
    try:
        next_page_url = soup.find(attrs={'class':"bloko-button", "data-qa":"pager-next"}).attrs['href']
        url="https://spb.hh.ru"+next_page_url
    except:
        next_page_url = False
    
