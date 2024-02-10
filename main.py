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
song_uri = []

for title in titles:
    result = sp.search(q=f"track: {title} year: {date_to_travel.split('-')[0]}")
    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")
    else:
        song_uri.append(uri)
    

playlist_id = sp.user_playlist_create(user_id, name=f"{date_to_travel} Billboard 100", public=False)['id']
