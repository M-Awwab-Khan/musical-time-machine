from bs4 import BeautifulSoup
import requests


date_to_travel = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date_to_travel}/')

soup = BeautifulSoup(response.text, 'html.parser')
titles= [item.text.strip() for item in soup.select("li ul li h3")]
print(titles)