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
        "name": "Akustik Gecesi: Yerel Sanatçılar Buluşuyor",
        "description": "Gecemizde yerel sanatçılarımızın unutulmaz performansları sizi bekliyor. Müziğin keyfini birlikte çıkaralım!",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İstanbul",
        "category": "Konser",
        "tags": ["müzik", "canlı performans"],
        "latlng": [41.0082, 28.9784],
        "date": "2023-02-15",
        "time": "19:30:00",
        "price": 50.0
    },
    {
        "id": 2,
        "name": "Modern Sanat Sergisi: Yerel Sanatçıların İmzası",
        "description": "Bu sergide, yerel sanatçılarımızın modern sanat eserleriyle buluşacaksınız. Sanat dolu bir gün sizi bekliyor.",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Ankara",
        "category": "Sergi",
        "tags": ["sanat", "görsel sanatlar"],
        "latlng": [39.9334, 32.8597],
        "date": "2023-03-10",
        "time": "15:00:00",
        "price": 0.0
    },
    {
        "id": 3,
        "name": "Jazz Akşamı: Ünlü Jazz Sanatçıları Sahne Alıyor",
        "description": "Bu akşam, ünlü jazz sanatçıları sizi eşsiz performanslarıyla büyüleyecek. Unutulmaz bir müzik ziyafeti sizleri bekliyor.",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İzmir",
        "category": "Konser",
        "tags": ["müzik", "jazz"],
        "latlng": [38.4192, 27.1287],
        "date": "2023-02-20",
        "time": "20:00:00",
        "price": 60.0
    },
    {
        "id": 4,
        "name": "Fotoğraf Sergisi: Doğanın Güzelliği",
        "description": "Bu sergide, doğanın güzelliklerini yakalamış fotoğraf sanatçılarının eserleriyle tanışacaksınız. Doğayla buluşun!",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Antalya",
        "category": "Sergi",
        "tags": ["fotoğraf", "doğa"],
        "latlng": [36.8969, 30.7133],
        "date": "2024-03-15",
        "time": "14:00:00",
        "price": 0.0
    },
    {
        "id": 5,
        "name": "Rock Festivali: Efsane Gruplar Bir Arada",
        "description": "Bu festivalde, efsane rock grupları sahnede! Unutulmaz anlar ve yüksek enerji sizleri bekliyor.",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Bursa",
        "category": "Konser",
        "tags": ["müzik", "rock"],
        "latlng": [40.1824, 29.0670],
        "date": "2024-02-25",
        "time": "18:00:00",
        "price": 75.0
    },
    {
        "id": 46,
        "name": "Yoga ve Meditasyon: Zihin ve Beden Sağlığı",
        "description": "Bu online seminerde, yoga ve meditasyonun zihin ve beden sağlığına olan olumlu etkilerini keşfedin. Kendinize zaman ayırın!",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Online",
        "category": "Online Seminer",
        "tags": ["sağlık", "yoga"],
        "latlng": [38.9637, 35.2433],
        "date": "2024-04-10",
        "time": "17:30:00",
        "price": 0.0
    },
    {
        "id": 47,
        "name": "Teknoloji Geliştirme Workshop'u",
        "description": "Bu etkinlikte, teknoloji geliştirme konusunda uzmanlarla bir araya gelin. Yenilikçi projeler ve stratejiler keşfedin!",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İstanbul",
        "category": "Workshop",
        "tags": ["teknoloji", "inovasyon"],
        "latlng": [41.0082, 28.9784],
        "date": "2024-04-20",
        "time": "14:00:00",
        "price": 30.0
    },
    {
        "id": 48,
        "name": "Klasik Müzik Konseri: Büyük Orkestra",
        "description": "Büyük orkestranın eşsiz performansını dinleyin. Klasik müziğin büyüsüne kapılacaksınız.",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Ankara",
        "category": "Konser",
        "tags": ["müzik", "klasik"],
        "latlng": [39.9334, 32.8597],
        "date": "2024-03-30",
        "time": "20:00:00",
        "price": 55.0
    },
    {
        "id": 49,
        "name": "Fotoğrafçılık Atölyesi: Temel Teknikler",
        "description": "Bu atölyede, temel fotoğrafçılık tekniklerini öğrenerek kendi görsel hikayenizi oluşturun. Fotoğraf dünyasına adım atın!",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İzmir",
        "category": "Atölye",
        "tags": ["fotoğraf", "eğitim"],
        "latlng": [38.4192, 27.1287],
        "date": "2024-04-05",
        "time": "16:30:00",
        "price": 40.0
    },
    {
        "id": 50,
        "name": "Popüler Bilim Konferansı: Evrende Yaşam Arayışı",
        "description": "Uzay bilimcilerle birlikte evrende yaşam arayışına dair son gelişmeleri keşfedin. Bilim dolu bir akşam sizi bekliyor!",
        "sliderImg": "https://picsum.photos/seed/picsum/1200/400",
        "coverImg": "https://picsum.photos/seed/picsum/200/300",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Bursa",
        "category": "Konferans",
        "tags": ["bilim", "uzay"],
        "latlng": [40.1824, 29.0670],
        "date": "2024-03-25",
        "time": "19:00:00",
        "price": 25.0
    },
       {
        "id": 51,
        "name": "Elektronik Müzik Partisi: DJ Performanslarıyla Dolu Gece",
        "description": "Elektronik müziğin ritmiyle dolu bir geceye hazır mısınız? Ünlü DJ'lerin performansları sizi bekliyor!",
        "sliderImg": "https://source.unsplash.com/1200x400/?electronic",
        "coverImg": "https://source.unsplash.com/200x300/?electronic",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İstanbul",
        "category": "Konser",
        "tags": ["müzik", "elektronik"],
        "latlng": [41.0082, 28.9784],
        "date": "2024-05-12",
        "time": "22:00:00",
        "price": 70.0
    },
    {
        "id": 52,
        "name": "Heykeltıraş Atölyesi: Taşın Ruhunu Keşfedin",
        "description": "Bu atölyede, heykeltıraşlarla birlikte taşın ruhunu keşfedin. Kendi heykelinizi yaratma şansı sizi bekliyor!",
        "sliderImg": "https://source.unsplash.com/1200x400/?sculpture",
        "coverImg": "https://source.unsplash.com/200x300/?sculpture",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Ankara",
        "category": "Atölye",
        "tags": ["sanat", "heykel"],
        "latlng": [39.9334, 32.8597],
        "date": "2024-06-05",
        "time": "14:00:00",
        "price": 45.0
    },
    {
        "id": 53,
        "name": "Komedya Akşamı: Gülmekten Yorulacaksınız!",
        "description": "Komedyenlerin eğlenceli performanslarıyla dolu bir akşam geçirin. Gülmekten yorulacaksınız!",
        "sliderImg": "https://source.unsplash.com/1200x400/?comedy",
        "coverImg": "https://source.unsplash.com/200x300/?comedy",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İzmir",
        "category": "Gösteri",
        "tags": ["komedi", "eğlence"],
        "latlng": [38.4192, 27.1287],
        "date": "2024-05-20",
        "time": "19:30:00",
        "price": 35.0
    },
    {
        "id": 54,
        "name": "Folk Müzik Festivali: Geleneksel Melodilerle Dolu Gün",
        "description": "Bu festivalde, geleneksel folk müziğinin güzelliklerini keşfedin. Canlı performanslar ve danslar sizi bekliyor!",
        "sliderImg": "https://source.unsplash.com/1200x400/?folk",
        "coverImg": "https://source.unsplash.com/200x300/?folk",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Bursa",
        "category": "Festival",
        "tags": ["müzik", "folk"],
        "latlng": [40.1824, 29.0670],
        "date": "2024-06-15",
        "time": "17:00:00",
        "price": 55.0
    },
    {
        "id": 55,
        "name": "Gastronomi Workshop'u: Lezzetli Tarifler",
        "description": "Bu workshop'ta, şeflerle birlikte lezzetli tarifleri öğrenin. Mutfakta ustalaşın!",
        "sliderImg": "https://source.unsplash.com/1200x400/?cooking",
        "coverImg": "https://source.unsplash.com/200x300/?cooking",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Antalya",
        "category": "Workshop",
        "tags": ["gastronomi", "yemek"],
        "latlng": [36.8969, 30.7133],
        "date": "2024-07-01",
        "time": "16:00:00",
        "price": 60.0
    },
    {
        "id": 56,
        "name": "Hip-Hop Dans Yarışması: En İyi Dansçıları İzleyin",
        "description": "Bu etkinlikte, en iyi hip-hop dansçılarının yarıştığı bir gösteri izleyin. Dans dolu bir gün sizi bekliyor!",
        "sliderImg": "https://source.unsplash.com/1200x400/?hiphop",
        "coverImg": "https://source.unsplash.com/200x300/?hiphop",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İstanbul",
        "category": "Dans",
        "tags": ["hip-hop", "dans"],
        "latlng": [41.0082, 28.9784],
        "date": "2023-07-10",
        "time": "20:30:00",
        "price": 40.0
    },
    {
        "id": 57,
        "name": "Bilim Kurgu Film Gecesi: Uzak Galaksilere Yolculuk",
        "description": "Bu film gecesinde, uzak galaksilere yolculuk eden bilim kurgu filmlerini izleyin. Sinema keyfi sizi bekliyor!",
        "sliderImg": "https://source.unsplash.com/1200x400/?scifi",
        "coverImg": "https://source.unsplash.com/200x300/?scifi",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Ankara",
        "category": "Film Gösterimi",
        "tags": ["bilim kurgu", "film"],
        "latlng": [39.9334, 32.8597],
        "date": "2023-07-25",
        "time": "21:00:00",
        "price": 25.0
    },
    {
        "id": 58,
        "name": "Gitar Çalma Atölyesi: Temel Akorlar",
        "description": "Bu atölyede, gitar çalmayı öğrenin ve temel akorları pratiğe dökün. Müzikle dolu anlar yaşayın!",
        "sliderImg": "https://source.unsplash.com/1200x400/?guitar",
        "coverImg": "https://source.unsplash.com/200x300/?guitar",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İzmir",
        "category": "Atölye",
        "tags": ["müzik", "enstrüman"],
        "latlng": [38.4192, 27.1287],
        "date": "2023-08-05",
        "time": "18:30:00",
        "price": 20.0
    },
    {
        "id": 59,
        "name": "Moda Defilesi: Yerel Tasarımcıların İlham Verici Koleksiyonları",
        "description": "Bu moda defilesinde, yerel tasarımcıların ilham verici koleksiyonlarını izleyin. Moda tutkunları buraya!",
        "sliderImg": "https://source.unsplash.com/1200x400/?fashion",
        "coverImg": "https://source.unsplash.com/200x300/?fashion",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Bursa",
        "category": "Defile",
        "tags": ["moda", "tasarım"],
        "latlng": [40.1824, 29.0670],
        "date": "2023-08-20",
        "time": "17:30:00",
        "price": 15.0
    },
    {
        "id": 60,
        "name": "Drama Oyunu: Duygusal Bir Yolculuk",
        "description": "Bu drama oyununda, duygusal bir yolculuğa çıkın. Oyuncuların etkileyici performanslarını izleyin!",
        "sliderImg": "https://source.unsplash.com/1200x400/?drama",
        "coverImg": "https://source.unsplash.com/200x300/?drama",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Antalya",
        "category": "Tiyatro",
        "tags": ["drama", "oyun"],
        "latlng": [36.8969, 30.7133],
        "date": "2023-09-05",
        "time": "19:00:00",
        "price": 25.0
    },
    {
        "id": 61,
        "name": "Edebiyat Sohbetleri: Ünlü Yazarlarla Buluşma",
        "description": "Bu etkinlikte, ünlü yazarlarla edebiyat sohbetlerine katılın. Kitap tutkunları buraya!",
        "sliderImg": "https://source.unsplash.com/1200x400/?literature",
        "coverImg": "https://source.unsplash.com/200x300/?literature",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İstanbul",
        "category": "Sohbet",
        "tags": ["edebiyat", "yazar"],
        "latlng": [41.0082, 28.9784],
        "date": "2023-09-20",
        "time": "18:00:00",
        "price": 0.0
    },
    {
        "id": 62,
        "name": "Bale Gösterisi: Zarif Hareketlerle Büyülü Anlar",
        "description": "Bu bale gösterisinde, zarif hareketlerle büyülü anlar yaşayın. Sanat dolu bir akşam sizi bekliyor!",
        "sliderImg": "https://source.unsplash.com/1200x400/?ballet",
        "coverImg": "https://source.unsplash.com/200x300/?ballet",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "Ankara",
        "category": "Bale",
        "tags": ["sanat", "bale"],
        "latlng": [39.9334, 32.8597],
        "date": "2023-10-01",
        "time": "20:00:00",
        "price": 50.0
    },
    {
        "id": 63,
        "name": "Gökyüzü Gözlem Etkinliği: Yıldızlarla Buluşma",
        "description": "Bu etkinlikte, gökyüzündeki yıldızları izlemek için bir araya gelin. Gözlemci dostları buraya!",
        "sliderImg": "https://source.unsplash.com/1200x400/?astronomy",
        "coverImg": "https://source.unsplash.com/200x300/?astronomy",
        "featured": True,
        "upcoming": True,
        "past": False,
        "location": "İzmir",
        "category": "Gözlem",
        "tags": ["astronomi", "gökyüzü"],
        "latlng": [38.4192, 27.1287],
        "date": "2023-10-15",
        "time": "22:30:00",
        "price": 10.0
    },
]



