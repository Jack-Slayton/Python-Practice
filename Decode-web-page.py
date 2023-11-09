from bs4 import BeautifulSoup
import requests
url = 'https://www.codermerlin.academy/users/jack-slayton/Digital%20Portfolio/index.html'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html)
print(soup)