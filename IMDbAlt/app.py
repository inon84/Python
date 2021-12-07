import requests
import uvicorn
from fastapi import FastAPI
import jsonify

app = FastAPI()

POPULAR_MOVIES_URL = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"
QUERYSTRING = {"homeCountry":"US","purchaseCountry":"US","currentCountry":"US"}
#TODO: Hide the rapidapi-key in env variables
HEADERS = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "321f72bce3msh7161ef254383001p1b98b3jsn3d9b8c33523d"
    }
response = requests.request("GET", POPULAR_MOVIES_URL,
                            headers=HEADERS, params=QUERYSTRING).json()

popular_movies = []
def clean_movies_list():
    for movie in response:
        movie = movie.split('/')[2]
        popular_movies.append(movie)
    return popular_movies

clean_movies_list()

def get_movie_details(title_id):
    GET_DETAILS_URL = "https://imdb8.p.rapidapi.com/title/get-details"
    QUERYSTRING = {"tconst":{ title_id }}
    movie_details = requests.request("GET", GET_DETAILS_URL, headers=HEADERS, 
                                     params=QUERYSTRING).json()
    return movie_details

# print(get_movie_details('tt0133093'))

'''
schema: 
['{"@type":"imdb.api.title.title",
"id":"/title/tt11214590/",
"image":{"height":1600,
"id":"/title/tt11214590/images/rm1248389377",
"url":"https://m.media-amazon.com/images/M/MV5BYzdlMTMyZWQtZWNmMC00MTJiLWIyMWMtM2ZlZDdlYzZhNTc0XkEyXkFqcGdeQXVyMTMzNDE5NDM2._V1_.jpg",
"width":1080},
"runningTimeInMinutes":158,
"title":"House of Gucci",
"titleType":"movie",
"year":2021}']
'''

class Movie():
    id = get_movie_details

def get_top_movies_details(limit=3):
    top_3_movies = []
    for movie in popular_movies[:limit]:
        top_3_movies.append(get_movie_details(movie))
    return top_3_movies

@app.get('/')
async def root():
    return get_top_movies_details(10)

# @app.post('/')
# async def root():
#     return get_movie_details('tt0133093')

# with open('IMDbAlt/bla.json', 'r') as file:
#     print(file.read())

if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8000, reload=True)