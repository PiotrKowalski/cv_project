  # -*- coding: utf-8 -*-
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup



response = urllib2.urlopen('https://myanimelist.net/anime/season')
html = response.read()
# print(html)

soup = BeautifulSoup(html, 'html.parser')

table = soup.findAll('div',attrs={"class":"seasonal-anime js-seasonal-anime"})
f = open("emited_episodes.txt", "w")

for key in table:
    print(key.find("p").getText())
    k = key.find("p").getText().encode('utf8')
    f.write(str(k)+"\n")

f.close()


