import requests
from bs4 import BeautifulSoup
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID="id"
SPOTIPY_CLIENT_SECRET="secret id"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="Day_46\\token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]
month = date.split("-")[1]
day = date.split("-")[2]

response=requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/").text
soup=BeautifulSoup(response,"lxml")
all=soup.find_all("h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
top=soup.find("h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
songs=[]
for i in all:
    songs.append(i.string)
songs = [str(s) for s in songs]
pattern = re.compile(r'^\W+|\W+$')
clean_tags = [re.sub(pattern, '', tag) for tag in songs]
clean_tags.insert(0,re.sub(pattern, '', top.string))

songs=[]
for song in clean_tags:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs.append(uri)
        print(songs)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, f"{year}-{month}-{day} Billboard 100")
playlist_id = playlist["id"]
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=songs)