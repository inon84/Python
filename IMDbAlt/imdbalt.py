import requests

POPULAR_MOVIES_URL = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"
querystring = {"homeCountry":"US","purchaseCountry":"US","currentCountry":"US"}
HEADERS = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "321f72bce3msh7161ef254383001p1b98b3jsn3d9b8c33523d"
    }
response = requests.request("GET", POPULAR_MOVIES_URL, headers=HEADERS, params=querystring).json()
# print(response.text)

popular_movies = []
def clean_movies_list():
    for movie in response:
        movie = movie.split('/')[2]
        popular_movies.append(movie)
    return popular_movies

print(clean_movies_list())

'''
doesn't work:
'''
def get_movie_details(title_id):
    title_id = title_id
    GET_DETAILS_URL = "https://imdb8.p.rapidapi.com/title/get-details"
    querystring = {"tconst":"{ title_id }"}
    movie_details = requests.request("GET", GET_DETAILS_URL, headers=HEADERS, params=querystring).text
    return movie_details

print(get_movie_details('tt0133093')) 
