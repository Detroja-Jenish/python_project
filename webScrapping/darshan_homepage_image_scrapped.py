from email.mime import image
from bs4 import BeautifulSoup
from csv import writer
import requests

url = "https://www.darshan.ac.in";

home_page = requests.get(url);
home_page_data = BeautifulSoup(home_page.content, "html.parser");

image_data = home_page_data.find_all("img")

print(len(image_data));

with open("iamge_urls.csv", 'w') as f:
    typewriter = writer(f);
    for img_source in image_data:
        ch = img_source['src'];
        string = ''.join(i for i in ch)
        typewriter.writerow(string)
        print(type(img_source['src']))