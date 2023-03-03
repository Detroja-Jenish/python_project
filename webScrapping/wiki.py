from bs4 import BeautifulSoup
import json
import requests

url = "https://en.wikipedia.org/wiki/List_of_bus_operating_companies"

page = requests.get(url);
pageData = BeautifulSoup(page.content, "html.parser");
print(pageData)

