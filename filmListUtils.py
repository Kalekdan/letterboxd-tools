import webScrapeUtils


def getCommonWatchlist(usernames):
    watchlists = []
    for user in usernames:
        userWatchlist = webScrapeUtils.getLetterboxdWatchlist(user)
        watchlists.append(userWatchlist)
    watchlistsSet = set(watchlists[0])
    for s in watchlists[1:]:
        watchlistsSet.intersection_update(s)
    print(watchlistsSet)
    
def getCommonWatchedList(usernames):
    watchedFilms = []
    for user in usernames:
        watchedFilms = watchedFilms + webScrapeUtils.getLetterboxdWatchedFilms(user)
    watchedFilmsSet = set(watchedFilms)
    return watchedFilmsSet

def findUnwatchedClassics(watchedList):
    # print(watchedList)
    imdbTop = webScrapeUtils.getIMDBTopX(3)
    print(list(set(imdbTop)-watchedList))

def getLetterboxdTopUnwatched(usernames, pagesToSearch=1):
    watchlistsSet = set()
    for user in usernames:
        userWatchlist = webScrapeUtils.getLetterboxdWatchedFilms(user)
        watchlistsSet.update(userWatchlist)
    topSet = set(webScrapeUtils.getLetterboxdTop(pagesToSearch))
    return topSet - watchlistsSet

#commonWatchedList = getCommonWatchedList(["jamesiam","kalekdan","aliiim","ayfex"])
#findUnwatchedClassics(commonWatchedList)

#commonWatchList = getCommonWatchlist(["baudehlaire","kalekdan","ayfex"])
#findUnwatchedClassics(commonWatchedList)
#getLetterboxdTop()
print(getLetterboxdTopUnwatched(["baudehlaire","kalekdan","ayfex","jamesiam","aliiim"], 25))
