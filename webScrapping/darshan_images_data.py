from bs4 import BeautifulSoup
import json
import requests

url = "https://www.darshan.ac.in";

home_page = requests.get(url);
home_page_data = BeautifulSoup(home_page.content, "html.parser");

image_data = home_page_data.find_all("img")

print(len(image_data));

img_data = []

for img_source in image_data:
        ch = img_source['src'];
        print(ch)
        img_data.append(ch);
        print()
        print('---------------------------------')
        print()
        print(type(img_source['src']))
        
with open("iamge_urls.json", 'w') as f:
	json.dump(img_data,f, indent=3);