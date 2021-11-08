import requests
from bs4 import BeautifulSoup

letterboxdURL = "https://letterboxd.com/"

def getPageFilms(username, urlPath, divClass):
    watchlist = []
    pageNum = 1
    while True:
        print("Scraping " + username + " " + urlPath + " page: " + str(pageNum))
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
    return getPageFilms(username, "watchlist", "poster-list -p125 -grid -scaled128")

def getWatchedFilms(username):
    return getPageFilms(username, "films", "poster-list -p70 -grid film-list clear")

def getRatedFilms(username):
    return getPageFilms(username, "films/ratings", "poster-list -p150 -grid")

def getRatings(username):
    ratings = {}
    pageNum = 1
    urlPath = "films/ratings"
    divClass = "poster-list -p150 -grid"
    while True:
        print("Scraping " + username + " " + urlPath + " page: " + str(pageNum))
        watchlistURL = letterboxdURL + username + '/'+ urlPath +'/page/' + str(pageNum)
        page = requests.get(watchlistURL)
        soup = BeautifulSoup(page.content, "html.parser")
        listHTML = soup.find_all("ul", {"class": divClass})
        if len(listHTML) == 0:
            return ratings
        li = listHTML[0].findChildren("li")
        if len(li) == 0:
            return ratings
        for film in li:
            name = film.find('img')['alt']
            rating = int(film.find('span', {"class":"rating"})['class'][1].split('-')[1])
            ratings[name] = rating
        pageNum = pageNum + 1

