from bs4 import BeautifulSoup as bs
import requests
import re
import methods
from pprint import pprint

URL = "https://comichron.com/monthlycomicssales/2019/2019-11.html"
page = requests.get(URL)

soup = bs(page.content, "html.parser")

results = soup.find(id="Top300Comics")

comics = results.find_all("tr")

comics_list = []

for comic in comics[1:11]:
    data = comic.find_all("td")
    comic_data = {
        "title": data[2].find("a").contents[0],
        "issue": int(
            re.sub("\D", "", data[3].text)
        ),  # use regex sub to discard any non-numeric characters.  May want to split instead so as to capture additional information.
        "price": float(data[4].text.strip("$")),
        # format change in 2017 to add "On Sale" date.  Adjusts list index to match.
        "publisher": data[5].text if len(data) == 7 else data[6].text,
        "units_sold": int(data[6].find("strong").text.replace(",", ""))
        if len(data) == 7
        else int(data[7].find("strong").text.replace(",", "")),
    }
    comics_list.append(comic_data)

pprint(comics_list)

# xmen345 = comics[1].find_all("td")
# for td in xmen345:
#     print(td)
#
# title = xmen345[2].find("a").contents[0]
# issue = int(xmen345[3].text)
# price = float(xmen345[4].text.strip("$"))
# publisher = xmen345[5].text
# units = int(xmen345[6].find("strong").text.replace(",", ""))
# print("Title:",title)
# print("Issue:", issue)
# print("Price:", price)
# print("Publisher:", publisher)
# print("Units Sold:", units)
