from bs4 import BeautifulSoup
import requests
import datetime

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#date = datetime.date.today()
date = "2023-09-23"
response = requests.get("https://www.billboard.com/charts/hot-100/"+date)

# with open("index.html") as file:
#     html_doc=file.read()
#
soup = BeautifulSoup(response.text,'html.parser')
song_name = soup.select("li ul li h3")
song = [song.getText().strip() for song in song_name]
print(song)
