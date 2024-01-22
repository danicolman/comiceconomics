from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

URL = "https://comichron.com/monthlycomicssales/1997/1997-04.html"
page = requests.get(URL)

soup = bs(page.content, "html.parser")

results = soup.find(id="Top300Comics")

comics = results.find_all("tr")

comics_list = []

for comic in comics[1:11]:
    data = comic.find_all("td")
    comic_data = {"title": data[2].find("a").contents[0], 
                  "issue": int(data[3].text), 
                  "price": float(data[4].text.strip("$")), 
                  "publisher": data[5].text, 
                  "units_sold": int(data[6].find("strong").text.replace(",", ""))}
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