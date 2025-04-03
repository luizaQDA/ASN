#Importando as bibliotecas

from bs4 import BeautifulSoup
import requests
import argparse
import random
import pandas as pd
import time

url = 'https://asn.flightsafety.org/asndb/type/_AT72/1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def extrair(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source=requests.get(url, headers=headers).text
    return source

aviacao = list()

for p in range(0, X): #Colocar a quantidade de páginas a serem raspadas no lugar de 'X' 
    url = f'https://asn.flightsafety.org/asndb/type/_AT72/{p}'
    extrair(url)
    tudo = extrair(url)
    soup = BeautifulSoup(tudo, 'html.parser')
    blocos = soup.find_all('tr', class_='list')
    for c in blocos:
        dicio = {'data': c.find('a').text.strip(),
             'modelo': c.find_all('td', class_='list')[1].text.strip(),
             'mortes': c.find_all('td', class_='list')[4].text.strip(),
             'local': c.find_all('td', class_='list')[5].text.strip()
        }
        aviacao.append(dicio)
print(aviacao)

df = pd.DataFrame(aviacao)
