from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

def make_url(year, month):
    return "https://comichron.com/monthlycomicssales/{year}/{year}-{month}.html".format(year=year, month=month)

def get_comics(url):
    page = requests.get(url)

    soup = bs(page.content, "html.parser")

    results = soup.find(id="Top300Comics")

    comics = results.find_all("tr")

    return comics

def find_columns(url):
    soup = bs(requests.get(url).content, "html.parser")
    table = soup.find("table", id="Top300Comics")
    headers = table.findAll("th")
    for header in headers:
        headers[headers.index(header)] = header.text
    return headers

dates = []
for year in range(1997, 2021):
    if year == 1997:
        monthrange = (4, 13)
    elif year == 2020:
        monthrange = (1, 4)
    else:
        monthrange = (1, 13)
    for month in range(monthrange[0], monthrange[1]):
        month = str(month) if len(str(month)) == 2 else "0" + str(month)
        dates.append((year, month))