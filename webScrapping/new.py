from bs4 import BeautifulSoup
import requests

url = "https://www.darshan.ac.in"

homepage = requests.get(url)

homepage_data = BeautifulSoup(homepage.text, 'html.parser');

print(homepage_data);
