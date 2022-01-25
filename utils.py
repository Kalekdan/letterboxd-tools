import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

letterboxdURL = "https://letterboxd.com/"
imdbURL = "https://www.imdb.com/"

def getLetterboxdPageFilms(username, urlPath, divClass, pages=-1):
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
        if pageNum == pages:
            return watchlist


def getLetterboxdJSPageFilms(username, urlPath, divClass, pages=-1):
    watchlist = []
    pageNum = 1
    session = HTMLSession()
    while True:
        print("Scraping " + username + " " + urlPath + " page: " + str(pageNum))
        watchlistURL = letterboxdURL + username + '/'+ urlPath +'/page/' + str(pageNum)
        page = session.get(watchlistURL)
        page.html.render()
        li = page.html.find("li."+ divClass +" img")
        if len(li) == 0:
            return watchlist
        for film in li:
            watchlist.append(film.attrs['alt'])
        pageNum = pageNum + 1
        if pageNum == pages:
            return watchlist

def getIMDBTopX(numberOfPagesToGet):
    topXList = []
    pageNum = 0
    while True:
        currentFilms = []
        print("Scraping IMDB page: " + str(pageNum))
        endString = ""
        if (pageNum > 0):
            endString = "&start=" + str((50* pageNum) + 1)
        topFilmsList = imdbURL + "search/title/?groups=top_" + str(numberOfPagesToGet * 50) + endString
        page = requests.get(topFilmsList)
        soup = BeautifulSoup(page.content, "html.parser")
        listHTML = soup.find_all("h3", {"class": "lister-item-header"})
        for film in listHTML:
            var = film.find("a").decode_contents()
            currentFilms.append(var)
        if len(currentFilms) > 0:
            pageNum += 1
            topXList = topXList + currentFilms
        else:
            break
    return topXList

def getLetterboxdWatchlist(username):
    return getLetterboxdPageFilms(username, "watchlist", "poster-list")

def getLetterboxdWatchedFilms(username):
    return getLetterboxdPageFilms(username, "films", "poster-list")

def getLetterboxdRatedFilms(username):
    return getLetterboxdPageFilms(username, "films/ratings", "poster-list")

def getLetterboxdTop(pages = 50):
    return getLetterboxdJSPageFilms("", "films/popular", "poster-container", pages)

def getLetterboxdRatings(username):
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