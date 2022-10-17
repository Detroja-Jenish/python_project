from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.imdb.com/calendar/?ref_=nv_mv_cal"
page = requests.get(url)
count = 0

print(page)

soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find_all("article", class_="sc-a299b883-1")

with open("releasing_movies_data.csv", 'w', encoding="utf8", newline="") as f:
	typewriter = writer(f)
	heading = ["movie_name", "featurig", "genre", "releasing_date"]
	typewriter.writerow(heading)
	for item in lists:
		date = item.find("h3", class_="ipc-title__text").text
		movie_container = item.find_all("ul", class_="ipc-metadata-list");
		for one_container in movie_container:
			movie_listed = one_container.find_all("li", class_="ipc-metadata-list-summary-item");
			for movies in movie_listed:
				movie_name = movies.find("a", class_="ipc-metadata-list-summary-item__t").text;
				sub_info = movies.find_all("ul", class_="ipc-inline-list")
				if(len(sub_info)>1):
					genre_list = sub_info[0].find_all("li", class_="ipc-inline-list__item");
					print(len(sub_info))
					genre_tupple= ((i.text + " : ") for i in genre_list)
					genre = " ".join(genre_tupple)
					actors_list = sub_info[1].find_all("li", class_="ipc-inline-list__item")
					actors_tupple = (i.text for i in actors_list)
					actors = " - ".join(actors_tupple)
					details = [movie_name, actors, genre, date];
					typewriter.writerow(details);
					count += 1
#print(date)

print("\n")


print(count)
print("\nnew begining.")
