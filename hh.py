#! /usr/local/bin/python3.8

import requests     
import json         
import time         
import os           
# import pandas as pd 

def  getVacancies():
    par = {'text': 'Data Engineering','per_page':'10', 'page':1}
    req = requests.get('https://api.hh.ru/vacancies',params=par)
    data = req.content.decode()
    req.close()
    pages = json.loads(data)
    v_ount = pages['found']
    pages = pages['pages']
    print ("<h1>Количество вакансий Data Engineering:", v_ount,'</h1>' )
    vacancies = json.loads(data)['items']
    for i in range(pages):
        par = {'text': 'Data Engineering','per_page':'10', 'page':i}
        req = requests.get('https://api.hh.ru/vacancies',params=par)
        data3 = req.content.decode()
#        print(data3)
        req.close()
        vacancies = json.loads(data3)['items']
        for vacancie in vacancies:
            
            req2=req = requests.get('https://api.hh.ru/employers/'+vacancie['employer']['id'])
            data2 = req2.content.decode()
            data2 = json.loads(data2)
            req2.close()
#            print(data2)
            ind=data2['industries']
            open_vacancies=data2['open_vacancies']
            if len(ind)>0:
                ind=ind[0]['name']
            else:
                ind=''
#            print(ind)
            print('<tr>')
            print('<td>',vacancie['name'],'</td><td>',vacancie['snippet']['requirement'],'</td><td>',open_vacancies,'</td><td>',ind,'</td>')
            print('</tr>')
#            exit()
    return vacancies

print ("Content-Type: text/html")
print ("")
print ('<html><table border=1>')
getVacancies()
print ('</table></html>')
