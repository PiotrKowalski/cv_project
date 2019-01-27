# -*- coding: utf-8 -*-
import requests
import json
import os
import sys
from django.template.defaultfilters import slugify
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
import django
django.setup()

from navbar.models import Genre

Genre.objects.all().delete()

array = []
for i in range(1, 40):
    query = '''
    query($perPage: Int, $page: Int){
        Page(page: $page, perPage: $perPage){
            media(type: ANIME){
                genres,
            }
        }
    }
    '''
    variables = {
        'page': i,
        'perPage': 50
    }
    url = 'https://graphql.anilist.co'

    response = requests.post(url, json={'query': query, 'variables': variables})
    data = json.loads(response.text)
    # print(json.loads(response.text))
    # print(json.dumps(data, sort_keys=True, indent=4))
    # with open(f'emitted_anime{i}.json', 'w') as outfile:
    #     json.dump(data, outfile)




    try :
        for k in data['data']['Page']['media']:
            genres = k['genres']

            # print(genres)

            for genre in genres:
                # print(genre)

                if (genre not in array):

                    array.append(genre)
                    print(array)
    except IndexError:
        break


with open('genres.txt', 'w') as outfile:
        for i in array:
            outfile.write(i+"\n")
            test = Genre(
                name=i,
            )
            test.save()
