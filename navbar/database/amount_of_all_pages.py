# -*- coding: utf-8 -*-
import requests
import json
import os
import time
import sys
from django.template.defaultfilters import slugify
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
import django
django.setup()



from navbar.models import Anime


hasNextPage = True
NextPage = 1


query = '''
    query($perPage: Int, $page: Int){
        Page(page: $page, perPage: $perPage){
            pageInfo {
                lastPage
            }
            media(type: ANIME){
                    id,
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
data = json.loads(response.text)
# print(json.dumps(data, sort_keys=True, indent=4))

print(data['data']['Page']['pageInfo']['lastPage'])
