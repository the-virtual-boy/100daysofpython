import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

config = dotenv_values("../.env")

CLIENT_ID = config["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = config["SPOTIFY_CLIENT_KEY"]
USER = config["SPOTIFY_USERNAME"]


time = input("What date would you like to travel back to? (YYYY-MM-DD): ")
# time = "2000-08-12"
response = requests.get("https://www.billboard.com/charts/hot-100/" + time)

page = response.text

soup = BeautifulSoup(page, "html.parser")

# song_tags = [soup.find(name="a", class_="c-title__link lrv-a-unstyle-link")]
# for tag in soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"):
#     song_tags.append(tag)

song_tags = soup.select("li ul li h3")
while song_tags == []:
    split_time = time.split("-")
    split_time[2] = str(int(split_time[2]) + 1)
    print(split_time, '-'.join(split_time))
    response = requests.get("https://www.billboard.com/charts/hot-100/" + '-'.join(split_time))
    page = response.text
    soup = BeautifulSoup(page, "html.parser")
    song_tags = soup.select("li ul li h3")
group_tags = soup.select("li ul li span")[::7]
songs = []
if song_tags ==  []:
    print("Sorry, no Billboard 100 for this day!")
    exit()
for song, group in zip(song_tags, group_tags):
    # print(f"{song_tags.index(song) + 1}: {song.getText().strip()}")
    songs.append(song.getText().strip() + " " + group.getText().strip())
print(song_tags, group_tags, songs)

scope = "playlist-modify-private playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://example.com", show_dialog=True, cache_path="token.txt", username=USER, scope=scope))
user_id = sp.current_user()["id"]
print(user_id)

results = ""
songs_toadd = []
for song in songs:
    results = sp.search(song)
    if len(results['tracks']['items']) > 0:
        songs_toadd.append(results['tracks']['items'][0]['uri'])

playlists = sp.user_playlists(user=user_id)
names = [i['name'] for i in playlists['items']]
print(names)
if f"back to {time}" not in names:
    playlist = sp.user_playlist_create(user=user_id, name=f"back to {time}", public=False, description=f"top 100 billboard on {time}")
else:
    for i in playlists['items']:
        if i['name'] == f"back to {time}":
            playlist = i
print(playlist)
sp.playlist_add_items(playlist_id=playlist['id'], items=songs_toadd)
