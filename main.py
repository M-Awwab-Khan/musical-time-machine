from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# date_to_travel = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
# response = requests.get(f'https://www.billboard.com/charts/hot-100/{date_to_travel}/')

# soup = BeautifulSoup(response.text, 'html.parser')
# titles= [item.text.strip() for item in soup.select("li ul li h3")]
# print(titles)