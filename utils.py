import requests
from bs4 import BeautifulSoup

letterboxdURL = "https://letterboxd.com/"


def getWatchlist(username):
    watchlist = []
    pageNum = 1
    while True:
        print("Scraping "+username+" watchlist page: " + str(pageNum))
        watchlistURL = letterboxdURL + username + '/watchlist/page/' + str(pageNum)
        page = requests.get(watchlistURL)
        soup = BeautifulSoup(page.content, "html.parser")
        listHTML = soup.find_all("ul", {"class": "poster-list -p125 -grid -scaled128"})
        if len(listHTML) == 0:
            return watchlist
        li = listHTML[0].findChildren("li")
        if len(li) == 0:
            return watchlist
        for film in li:
            watchlist.append(film.find('img')['alt'])
        pageNum = pageNum + 1

