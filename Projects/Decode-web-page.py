from bs4 import BeautifulSoup
import requests
url = 'https://github.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html)
print(soup)