  # -*- coding: utf-8 -*-
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup

from jikanpy import Jikan
import requests
import json

query = '''
query($perPage: Int, $page: Int){
    Page(page: $page, perPage: $perPage){
        media(type: ANIME, status: RELEASING){
            id,
            title{
                romaji,
                english
            }
            description
            startDate{
                year
                month
                day
            }
            endDate{
                year
                month
                day
            }
            genres
            status
        }
    }
}
'''
variables = {
    'page': 1,
    'perPage': 50
}
url = 'https://graphql.anilist.co'

response = requests.post(url, json={'query': query, 'variables': variables})
parsed = response.json()
print(json.dumps(parsed, sort_keys=True, indent=4))
with open('anime.json', 'w') as outfile:
    json.dump(parsed, outfile)

#
# jikan = Jikan()
#
# mushishi = jikan.anime(457)
#
#
# request = Request(f'https://private-anon-596419ef23-jikan.apiary-proxy.com/v3/genre/{type}/{genre_id}/{page}')
#
# response_body = urlopen(request).read()
# print(response_body)




# f = open("test.txt", "w")
#
# for key in mushishi:
#     print(key)
#
#     f.write(str(key)+"\n")
#
# f.close()

# response = urllib2.urlopen('https://myanimelist.net/anime.php')
# html = response.read()
# # print(html)
#
# soup = BeautifulSoup(html, 'html.parser')
#
# table = soup.findAll('div',attrs={"class":"genre-list al"})
# f = open("list_of_genres.txt", "w")
#
# for key in table:
#     print(key.find("a").getText())
#     k = key.find("a").getText().encode('utf8')
#     f.write(str(k)+"\n")
#
# f.close()
#

