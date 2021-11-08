import requests
from bs4 import BeautifulSoup

letterboxdURL = "https://letterboxd.com/"
imdbURL = "https://www.imdb.com/"


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
            topXList.append(currentFilms)
        else:
            break
    return topXList