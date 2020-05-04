from bs4 import BeautifulSoup as bs
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
source = requests.get('https://en.wikipedia.org/wiki/Secure_Shell', headers=headers).text

soup = bs(source, 'html.parser')
p = soup.find_all('p')

#print(soup.prettify())
for par in p:
	print(par)