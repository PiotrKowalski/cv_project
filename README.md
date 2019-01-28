# CV Project Website

Application is called "navbar" and holds sourcecode of the website.

Interesting things used in the project:

* Fetching database from [GraphQL API](https://github.com/PiotrKowalski/cv_project/blob/master/navbar/database/getting_a_test_probe.py)
* Using Q objects for dynamic filtering 
```python
def get_queryset(self):
    genres = self.request.GET.getlist('genres')
    type = self.request.GET.get('type')
    if len(genres) > 1:
        new_arr = []
        for key in genres:
            key = '{'+key+'}'
            new_arr.append(key)
        queries = [Q(genres_array__contains=genre) for genre in new_arr]
        query = queries.pop()
        if type == 'or':
            for item in queries:
                query |= item
        elif type == 'and':
            for item in queries:
                query &= item
        return Anime.objects.filter(query)
    elif len(genres) == 1:
        return Anime.objects.filter(genres_array__contains=genres)
    else:
        arr = []
        return arr
```
* Class based view approach to the project


The project is hosted on [heroku](https://piotr-cv-project.herokuapp.com/)
