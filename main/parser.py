from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from .models import Series

URL = 'https://www.investing.com/search/?q=Manufacturing%20Purchasing%20Managers&tab=ec_event'
driver = webdriver.Chrome(ChromeDriverManager().install())
request = driver.get(URL)


def get_series():
    page = driver.page_source
    page_soup = BeautifulSoup(page, 'html.parser')
    containers = page_soup.findAll("a", {"class":"row"})

    for s in containers:
        href = s.get("href")
        if not "equities" in href:
            url = "https://www.investing.com" + href

        for title in s.findAll("span", {"class": "fourth"}):
            if not "Equity" in title.text:
                title = title.text

        record = Series.objects.create(title=title, url=url)
