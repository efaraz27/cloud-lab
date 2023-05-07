import requests
from bs4 import BeautifulSoup

n = 10

url = f"https://www.imdb.com/chart/top?ref_=nv_mv_250"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movie_tags = soup.select("td.titleColumn a")
rating_tags = soup.select("td.posterColumn span[name='ir']")

for i in range(n):
    movie_tag = movie_tags[i]
    rating_tag = rating_tags[i]

    movie_url = f"https://www.imdb.com{movie_tag['href']}"

    movie_response = requests.get(movie_url)
    movie_soup = BeautifulSoup(movie_response.text, "html.parser")

    genre_tags = movie_soup.select("div.subtext a[href^='/genre/']")
    genres = [tag.text for tag in genre_tags]

    print(f"Title: {movie_tag.text}")
    print(f"Genres: {', '.join(genres)}")
    print(f"Rating: {rating_tag['data-value']}")
    print(f"URL: {movie_url}")
    print()
