import requests
from bs4 import BeautifulSoup

letterboxdURL = "https://letterboxd.com/"


def getWatchlist(username):
    watchlist = []
    watchlistURL = letterboxdURL + username + '/watchlist'
    page = requests.get(watchlistURL)
    soup = BeautifulSoup(page.content, "html.parser")
    listHTML = soup.find_all("ul", {"class": "poster-list -p125 -grid -scaled128"})
    if len(listHTML) == 0:
        return []
    li = listHTML[0].findChildren("li")
    for film in li:
        watchlist.append(film.find('img')['alt'])
    return watchlist