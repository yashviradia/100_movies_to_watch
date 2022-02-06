import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
sorted_titles = []

for title in movie_titles:
    sorted_titles.append(title.getText())

sorted_titles.reverse()

with open("./100_movies_to_watch.txt", mode="w") as movie_titles_file:
    for title in sorted_titles:
        movie_titles_file.write(f"{title}\n")