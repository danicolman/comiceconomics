# imports as needed
from bs4 import BeautifulSoup as bs
import re


class Issue:  # now takes headers directly from input url; no longer sensitive to table format change.
    def __init__(self, comics, headers):
        data = comics.contents
        self.title = data[headers.index("Comic-book Title")].text
        self.issue = re.sub(
            "\D",
            "",
            data[headers.index("Issue")].text
            if not data[headers.index("Issue")].text == ""
            else "0",
        )
        self.price = float(data[headers.index("Price")].text.strip("$"))
        self.publisher = data[headers.index("Publisher")].text
        self.units_sold = int(
            data[headers.index("Est. units")].find("strong").text.replace(",", "")
        )

    def sales_report(self):
        print(
            f"Issue {self.issue} of {self.title} from {self.publisher} sold {self.units_sold} units at a cover price of ${self.price}."
        )


# test_comic = Issue(
#     bs(
#         '<tr><td data-order="13">13</td><td data-order="13">13</td><td><a href="https://www.ebay.com/sch/Comics/259104/i.html?_from=R40&amp;_nkw=Venom+20+2019" rel="nofollow" target="_blank" title="See current eBay listings for this issue">Venom</a></td><td>20</td><td>$3.99</td><td>11/27/19</td><td>Marvel</td><td><strong>67,702</strong></td></tr>',
#         "html.parser",
#     )
# )

# print(
#     f"Issue {test_comic.issue} of {test_comic.title} from {test_comic.publisher} sold {test_comic.units_sold} unites at a cover price of ${test_comic.price}."
# )
