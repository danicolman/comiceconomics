from bs4 import BeautifulSoup as bs
import requests
import re
from methods import make_urls, get_comics, find_columns
from pprint import pprint
from classes import Issue

# URL = "https://comichron.com/monthlycomicssales/2019/2019-11.html"
# page = requests.get(URL)

# soup = bs(page.content, "html.parser")

# results = soup.find(id="Top300Comics")

# comics = results.find_all("tr")

# comics_list = []

for url in make_urls()[270:]:
    print(url)
    headers = find_columns(url)
    comics = get_comics(url)[1:]
    for comic in comics[:5]:
        Issue(comic, headers).sales_report()

# how do I take the month & year from the url constructor and turn it into datetime information?
