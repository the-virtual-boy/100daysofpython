import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")
# print(soup.prettify())

movie_tags = soup.find_all(name="h3", class_="title")
# print(movie_tags)
movies = []
for title in movie_tags:
    movies.append(title.getText())
print(movies[::-1])
movies = movies[::-1]
with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
