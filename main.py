from time import time
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
    "https://demo1.fullstacksamurai.online"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>findEvents API | FastAPI Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                 
            </ul>
            
        </div>
    </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}

""" Returns an array of events """
@app.get("/events")
async def get_events():
    """ Structure: Slider Img, Cover Img, Featured, Upcoming, Past, Location, Category, tags, latlng, date, time, price  """
    return [
        {
            "id": 1,
            "name": "Event 1",
            "description": "This is the description for Event 1",
            "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
            "coverImg": "https://picsum.photos/seed/picsum/200/300",
            "featured": True,
            "upcoming": True,
            "past": False,
            "location": "Location 1",
            "category": "Category 1",
            "tags": ["tag1", "tag2", "tag3"],
            "latlng": [1.0, 2.0],
            "date": "2021-01-01",
            "time": "12:00:00",
            "price": 100.0,
        },
        {
            "id": 2,
            "name": "Event 2",
            "description": "This is the description for Event 2",
            "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
            "coverImg": "https://picsum.photos/seed/picsum/200/300",
            "featured": False,
            "upcoming": True,
            "past": False,
            "location": "Location 2",
            "category": "Category 2",
            "tags": ["tag1", "tag2", "tag3"],
            "latlng": [1.0, 2.0],
            "date": "2021-01-01",
            "time": "12:00:00",
            "price": 100.0,
        },
        {
            "id": 3,
            "name": "Event 3",
            "description": "This is the description for Event 3",
            "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
            "coverImg": "https://picsum.photos/seed/picsum/200/300",
            "featured": False,
            "upcoming": True,
            "past": False,
            "location": "Location 3",
            "category": "Category 3",
            "tags": ["tag1", "tag2", "tag3"],
            "latlng": [1.0, 2.0],
            "date": "2021-01-01",
            "time": "12:00:00",
            "price": 100.0,
        },
        {
            "id": 4,
            "name": "Event 4",
            "description": "This is the description for Event 4",
            "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
            "coverImg": "https://picsum.photos/seed/picsum/200/300",
            "featured": False,
            "upcoming": True,
            "past": False,
            "location": "Location 4",
            "category": "Category 4",
            "tags": ["tag1", "tag2", "tag3"],
            "latlng": [1.0, 2.0],
            "date": "2021-01-01",
            "time": "12:00:00",
            "price": 100.0,
        },
        {
            "id": 5,
            "name": "Event 5",
            "description": "This is the description for Event 5",
            "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
            "coverImg": "https://picsum.photos/seed/picsum/200/300",
            "featured": False,
            "upcoming": True,
            "past": False,
            "location": "Location 5",
            "category": "Category 5",
            "tags": ["tag1", "tag2", "tag3"],
            "latlng": [1.0, 2.0],
            "date": "2021-01-01",
            "time": "12:00:00",
            "price": 100.0,
        },
        {
            "id": 6,
            "name": "Event 6",
            "description": "This is the description for Event 6",
            "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
            "coverImg": "https://picsum.photos/seed/picsum/200/300",
            "featured": False,
            "upcoming": True,
            "past": False,
            "location": "Location 6",
            "category": "Category 6",
            "tags": ["tag1", "tag2", "tag3"],
            "latlng": [1.0, 2.0],
            "date": "2021-01-01",
            "time": "12:00:00",
            "price": 100.0,
        },
    ]


