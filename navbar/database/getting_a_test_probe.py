# -*- coding: utf-8 -*-
import requests
import json
import os
import time
import sys
from django.template.defaultfilters import slugify
from django.utils.text import slugify
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

import django
django.setup()

from navbar.models import Anime


Anime.objects.all().delete()

hasNextPage = True
NextPage = 220

while(hasNextPage):
    query = '''
        query($perPage: Int, $page: Int){
            Page(page: $page, perPage: $perPage){
                pageInfo {
                    total,
                    hasNextPage
                 }
                media(type: ANIME){
                    id,
                    title{
                        romaji,,
                        english,
                    }
                    type,
                    status,
                    description,
                    startDate{
                        year,
                        month,
                        day,
                    }
                    endDate{
                        year,
                        month,
                        day,
                    }
                    season,
                    episodes,
                    duration,
                    genres,
                    averageScore,
                    trending,
                    popularity,
                    streamingEpisodes {
                        title,
                        url,
                    }
                    coverImage {
                        large,
                        medium,
                    }
                    bannerImage,
                    isAdult,
                    format,
                }
            }
        }
        '''
    variables = {
        'page': NextPage,
        'perPage': 50
    }
    url = 'https://graphql.anilist.co'

    response = requests.post(url, json={'query': query, 'variables': variables})
    data = json.loads(response.text)
    # print(json.dumps(data, sort_keys=True, indent=4))
    # with open(f'database_all/all_anime{NextPage}.json', 'w') as outfile:
    #     json.dump(data, outfile)
    # if data['data']['Page']['pageInfo']['hasNextPage'][0] is not None:
    try:
        hasNextPage = data['data']['Page']['pageInfo']['hasNextPage']
    except TypeError:
        print("blad")
        NextPage += 1

    NextPage += 1
    time.sleep(1)

    try:
        data['data']['Page']['media']
    except TypeError:
        print("blad2")
        continue

    for k in data['data']['Page']['media']:


        startDateDay = k['startDate']['day']
        startDateMonth = k['startDate']['month']
        startDateYear = k['startDate']['year']
        endDateDay = k['endDate']['day']
        endDateMonth = k['endDate']['month']
        endDateYear = k['endDate']['year']

        if (startDateDay is None or startDateMonth is None or startDateYear is None) or \
                (startDateDay not in range(0, 31) or startDateMonth not in range(0, 12)):
            startDateYear = 1
            startDateMonth = 1
            startDateDay = 1

        if (endDateDay is None or endDateMonth is None or endDateYear is None) or \
                (endDateYear not in range(0, 31) or endDateMonth not in range(0, 12)):
            endDateYear = 1
            endDateMonth = 1
            endDateDay = 1

        title = k['title']['romaji']
        url = slugify(k['title']['romaji'])
        if not url.strip():
            url = 'no-title'




        # print(startDateMonth)

        # episode_array_len = len(k['streamingEpisodes'])
        # print(episode_array_len)
        # if (episode_array_len):
        #     for i in range(episode_array_len):
        #         print(k['streamingEpisodes'][i])
        #         print(k['streamingEpisodes'][i]['title'],k['streamingEpisodes'][i]['url'])

        #         test = Anime(
        #             streaming_episodes=[k['streamingEpisodes'][i]['title'],k['streamingEpisodes'][i]['url']],
        #         test.save()
        #
        # try:
        print(k['id'])
        # print(k['title'])
        # print(k['streamingEpisodes'])
        test = Anime(
            id_API=k['id'],
            title=k['title']['romaji'],
            url=url,
            # url=slugify(k['title']['romaji']),
            type=k['type'],
            description=k['description'],
            status=k['status'],
            season=k['season'],
            episodes=k['episodes'],
            duration=k['duration'],
            genres=k['genres'],
            genres_array=k['genres'],
            average_score=k['averageScore'],
            trending=k['trending'],
            popularity=k['popularity'],
            streaming_episodes_JSON=k['streamingEpisodes'],
            imageURL=k['coverImage']['large'],
            imageURL_medium=k['coverImage']['medium'],
            start_date=datetime.date(startDateYear,startDateMonth,startDateDay),
            end_date=datetime.date(endDateYear, endDateMonth, endDateDay),
            banner_image=k['bannerImage'],
            is_adult=k['isAdult'],
            media_format=k['format'],
            )
        test.save()

        # except IndexError:
        #     continue



