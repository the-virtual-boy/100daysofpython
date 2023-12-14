# Spotify Playlist Time Machine

Day 46 cotinued the use of BeautifulSoup with a project that took a date in the format of `YYYY-MM-DD` from the user, and scraped (Billboards hot 100 charts)[https://www.billboard.com/charts/hot-100/] to find what were the top 100 songs on the charts on that day, then used the (Spotipy Python module for Spotify)[https://spotipy.readthedocs.io/en/2.22.1/] to create a spotify playlist with those top 100 songs.

This was definitely more fun than the previous day's project, and gave the added bonus of being hit with a nostalgia punch when listening to the big radio hits from when I was a kid. The hardest parts was definitely getting the exact info I needed from the top 100 billboard that would give me an accurate search in spotify, as just searching the name of the song often times gave me a completely different song of the same name. The simple answer was just to make sure to scrape the song name and group and use both in the search query. 
