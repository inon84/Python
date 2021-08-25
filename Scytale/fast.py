import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/static', StaticFiles(directory='static/'), name='static')
templates = Jinja2Templates(directory='templates/')


@app.get('/prs', response_class=HTMLResponse)
async def read_items(request: Request):
    # return "GET."
    result = 'TEST'
    # return templates.TemplateResponse('index.html', 'request': request)
    return templates.TemplateResponse('index.html', context={'request': request})

@app.post('/prs', response_class=HTMLResponse)
async def search(context):
    # return 'POST', context
    return templates.TemplateResponse('index.html')

if __name__ == '__main__':
    uvicorn.run('fast:app', host='localhost', port=8000, reload=True)
