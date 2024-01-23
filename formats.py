from bs4 import BeautifulSoup as bs
import requests


# programmatically generate urls for dates in range
def make_urls():
    base_url = "https://comichron.com/monthlycomicssales/{year}/{year}-{month}.html"

    urls = []

    for year in range(1997, 2021):
        if year == 1997:
            monthrange = (4, 13)
        elif year == 2020:
            monthrange = (1, 4)
        else:
            monthrange = (1, 13)
        for month in range(monthrange[0], monthrange[1]):
            month = str(month) if len(str(month)) == 2 else "0" + str(month)
            urls.append(base_url.format(year=year, month=month))

    return urls


def find_columns(url):
    soup = bs(requests.get(url).content, "html.parser")
    table = soup.find("table", id="Top300Comics")
    headers = table.findAll("th")
    return headers


for url in make_urls():
    if len(find_columns(url)) == 7:
        print(url)
    else:
        print(url.upper())
