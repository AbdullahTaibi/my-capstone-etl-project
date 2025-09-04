import requests
from bs4 import BeautifulSoup

def scrape_flags():
    url = "https://www.worldometers.info/geography/flags-of-the-world/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    flags = {}
    for img in soup.find_all("img"):
        country = img.get("alt")
        flag_url = "https://www.worldometers.info" + img.get("src")
        if country and flag_url:
            flags[country] = flag_url
    return flags