from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()['id']
date_to_travel = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date_to_travel}/')

soup = BeautifulSoup(response.text, 'html.parser')
titles= [item.text.strip() for item in soup.select("li ul li h3")]
results = sp.search(q=f"track: {titles[0]} year: {date_to_travel.split('-')[0]}", limit=1)
pprint(results)