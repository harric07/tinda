import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd



example_url = "https://en.wikipedia.org/wiki/Comparison_of_programming_languages"


url = example_url

def scrape_for_data(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.findAll("table", {"class": "wikitable"})[0]
    rows = table.findAll("tr")
    with open("data.csv", "wt+", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            csv_row = []
            for cell in row.findAll(["td", "th"]):
                csv_row.append(cell.get_text())
            writer.writerow(csv_row)
    x = pd.read_csv("data.csv")
    x.head()

# scrape_for_data(url)
