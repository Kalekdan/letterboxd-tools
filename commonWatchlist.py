import utils


def getCommonWatchlist(usernames):
    watchlists = []
    for user in usernames:
        userWatchlist = utils.getWatchlist(user)
        watchlists.append(userWatchlist)
    watchlistsSet = set(watchlists[0])
    for s in watchlists[1:]:
        watchlistsSet.intersection_update(s)
    print(watchlistsSet)

getCommonWatchlist(["jamesiam","kalekdan"])
