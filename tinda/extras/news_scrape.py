# pip install googlenews

from GoogleNews import GoogleNews
import pandas as pd


def scrape_news(query):
    """
    Scrape news from Google News
    """
    news = GoogleNews(period='1d')
    news.search(query)
    result = news.result(query)
    # data = pd.DataFrame.from_dict(result)
    # data = data.drop(columns=["img"])
    # data.head()
    titles = []
    links = []
    for i in result:
        titles.append(i["title"])
        links.append(i["link"])
        print("Title : ", i["title"],".\n")
        print("News : ", i["desc"],".\n")
        print("Read Full News : ", i["link"],".\n")
        print("-----------------------------------------------------")
    cli_display = f"Titles: \n{titles}\nLinks: \n{links}"
    print("Titles: ")
    for i in titles:
        print(i)
    print("Links: ")
    for i in links:
        print(i)

# scrape_news("bitcoin")
