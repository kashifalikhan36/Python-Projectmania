from bs4 import BeautifulSoup
import lxml
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

soup=BeautifulSoup(response,"lxml")
all=soup.find_all("h3", class_="title")
movie=[]
for i in all:
    movie.append(i.string)
new_movie = list(reversed(movie))
print(new_movie)
with open("Day_45\movies.txt","w",encoding="utf-8") as file:
    for i in new_movie:
        file.write(f"{i}\n")
