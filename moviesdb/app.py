import requests
import uvicorn
from fastapi import FastAPI

'''
API Source Credits: https://www.themoviedb.org
'''

# /discover/movie?sort_by=popularity.desc
API_KEY = '77328f3d28e013fbe0a55f8c2313d876' #TODO hide this
# list_id = 0
# POPULAR_MOVIES_DESC = '/discover/movie?sort_by=popularity.desc'

# REQ_URL = 'https://api.themoviedb.org/4/list/{list_id}?page=1&api_key={API_KEY}&language=en'

app = FastAPI()

BASE_URL = f'https://api.themoviedb.org/4/discover/movis?sort_by=popularity.desc?page=1&language=en&api_key={API_KEY}'

payload = '{}'
headers = {
    'content-type': "application/json;charset=utf-8"
    }

response = requests.request("GET", BASE_URL, data=payload, headers=headers)

print(response.text)

@app.get('/')
async def root():
    return response

@app.post('/')
async def root():
    pass

if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8000, reload=True)