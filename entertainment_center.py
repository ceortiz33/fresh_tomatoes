from media import Movies
import fresh_tomatoes as ft
import urllib3
import json

http = urllib3.PoolManager()

r = http.request('GET','https://my-movies-api-project.herokuapp.com/movies')
data = json.loads(r.data.decode('utf-8'))

movies = []

for movie in data:
	movies.append(Movies(movie['name'], movie['image_poster_url'], movie['trailer_youtube_url']))

app = ft.open_movies_page(movies)