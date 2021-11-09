import utils


def getCommonWatchlist(usernames):
    watchlists = []
    for user in usernames:
        userWatchlist = utils.getLetterboxdWatchlist(user)
        watchlists.append(userWatchlist)
    watchlistsSet = set(watchlists[0])
    for s in watchlists[1:]:
        watchlistsSet.intersection_update(s)
    print(watchlistsSet)
    
def getCommonWatchedList(usernames):
    watchedFilms = []
    for user in usernames:
        watchedFilms = watchedFilms + utils.getLetterboxdWatchedFilms(user)
    watchedFilmsSet = set(watchedFilms)
    return watchedFilmsSet

def findUnwatchedClassics(watchedList):
    # print(watchedList)
    imdbTop = utils.getIMDBTopX(3)
    print(list(set(imdbTop)-watchedList))
            

commonWatchedList = getCommonWatchedList(["jamesiam","kalekdan","aliiim","ayfex"])
findUnwatchedClassics(commonWatchedList)

