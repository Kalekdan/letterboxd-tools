import requests
from bs4 import BeautifulSoup

letterboxdURL = "https://letterboxd.com/"

def getPageContent(username, urlPath, divClass):
    watchlist = []
    pageNum = 1
    while True:
        print("Scraping "+username+" watchlist page: " + str(pageNum))
        watchlistURL = letterboxdURL + username + '/'+ urlPath +'/page/' + str(pageNum)
        page = requests.get(watchlistURL)
        soup = BeautifulSoup(page.content, "html.parser")
        listHTML = soup.find_all("ul", {"class": divClass})
        if len(listHTML) == 0:
            return watchlist
        li = listHTML[0].findChildren("li")
        if len(li) == 0:
            return watchlist
        for film in li:
            watchlist.append(film.find('img')['alt'])
        pageNum = pageNum + 1

def getWatchlist(username):
    return getPageContent(username, "watchlist", "poster-list -p125 -grid -scaled128")

def getWatchedFilms(username):
    return getPageContent(username, "films", "poster-list -p70 -grid film-list clear")

