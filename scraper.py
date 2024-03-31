from bs4 import BeautifulSoup as bs
import requests
import re
from methods import make_url, get_comics, find_columns, dates
from pprint import pprint
from classes_copy import Issue
import xlsxwriter
import datetime
import pandas as pd

# for url in make_urls()[270:]:
#     print(url)
#     headers = find_columns(url)
#     comics = get_comics(url)[1:]
#     for comic in comics[:5]:
#         Issue(comic, headers).sales_report()

#messy notes clean this up later

with pd.ExcelWriter("datatest.xlsx") as writer:
    for date in dates:
        year, month = date
        url = make_url(*date)
        print(url)
        headers = find_columns(url)
        comics = get_comics(url)[1:]
        cl = []
    
        for comic in comics:
            c = {}
            for header in headers:
                # print(header, comic.contents[headers.index(header)].text)
                c.update({header: comic.contents[headers.index(header)].text})
            # pprint(c)
            cl.append(c)
        df = pd.DataFrame.from_dict(cl)
        df.to_excel(writer, sheet_name=datetime.date(year,int(month),1).strftime("%B, %Y"))