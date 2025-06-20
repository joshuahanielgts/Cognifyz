import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for i, title in enumerate(soup.find_all('h2'), 1):
        print(f"{i}. {title.text.strip()}")

scrape_titles("https://www.google.com/")
