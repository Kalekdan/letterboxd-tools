import os
import webScrapeUtils


class FilmGroupMember:
    def __init__(self, name, letterboxdUsername=None):
        self.name = name
        self.letterboxdUsername = letterboxdUsername
        self.letterboxdWatchList = []
        self.letterboxdWatchedFilms = []
        self.letterboxdRatedFilms = []
        self.letterboxdRatings = {}

    def retrieveLetterboxdWatchList(self):
        if self.letterboxdUsername != None:
            return webScrapeUtils.getLetterboxdWatchlist(self.letterboxdUsername)
        return

    def retrieveLetterboxdWatchedFilms(self):
        if self.letterboxdUsername != None:
            return webScrapeUtils.getLetterboxdWatchedFilms(self.letterboxdUsername)
        return

    def retrieveLetterboxdRatedFilms(self):
        if self.letterboxdUsername != None:
            return webScrapeUtils.getLetterboxdRatedFilms(self.letterboxdUsername)
        return

    def retrieveLetterboxdRatings(self):
        if self.letterboxdUsername != None:
            return webScrapeUtils.getLetterboxdRatings(self.letterboxdUsername)
        return

    def updateLetterboxdWatchList(self):
        self.letterboxdWatchList = self.retrieveLetterboxdWatchList()
        return

    def updateLetterboxdWatchedFilms(self):
        self.letterboxdWatchedFilms = self.retrieveLetterboxdWatchedFilms()
        return

    def updateLetterboxdRatedFilms(self):
        self.letterboxdRatedFilms = self.retrieveLetterboxdRatedFilms()
        return

    def updateLetterboxdRatings(self):
        self.letterboxdRatings = self.retrieveLetterboxdRatings()
        return

    def getLetterboxdWatchList(self):
        return self.letterboxdWatchList

    def getLetterboxdWatchedFilms(self):
        return self.letterboxdWatchedFilms

    def getLetterboxdRatedFilms(self):
        return self.letterboxdRatedFilms

    def getLetterboxdRatings(self):
        return self.letterboxdRatings


class FilmGroup:
    def __init__(self, groupName, members=[]):
        self.groupName = groupName
        self.members = members

    def addMember(self, newMember):
        if newMember in self.members:
            return
        self.members.append(newMember)

    def addMembers(self, newMembers):
        for member in newMembers:
            self.addMember(member)

    def removeMember(self, memberToRemove):
        if memberToRemove in self.members:
            self.members.remove(memberToRemove)
        return

    def getGroupName(self):
        return self.groupName

    def getMembers(self):
        return self.members

    def updateMembersLetterboxd(self):
        for member in self.getMembers():
            member.updateLetterboxdWatchList()
            member.updateLetterboxdWatchedFilms()
            member.updateLetterboxdRatedFilms()
            member.updateLetterboxdRatings()

    def __str__(self):
        return self.groupName


def saveFilmGroups(filmGroups):
    for filmGroup in filmGroups:
        members = filmGroup.getMembers()
        for member in members:
            memberPath = filmGroup.getGroupName() + "/" + member.name
            isExist = os.path.exists(memberPath)
            if not isExist:
                os.makedirs(memberPath)
            writeMemberDetailsFile(memberPath, member)
            writeMemberLetterboxdFiles(memberPath, member)


def writeMemberDetailsFile(root, member):
    f = open(root + "/" + member.name + ".properties", "w")
    f.write("name=" + member.name + "\n")
    f.write("letterboxdName=" + member.name + "\n")
    f.close()
    return

def writeMemberLetterboxdFiles(root, member):
    # Create dir
    letterboxdPath = root + "/letterboxd"
    isExist = os.path.exists(letterboxdPath)
    if not isExist:
        os.mkdir(letterboxdPath)
    # Write watchlist
    filmList = member.getLetterboxdWatchList()
    f = open(letterboxdPath + "/watchlist.txt", "w")
    for film in filmList:
        f.write(film + "\n")
    f.close()
    # Write watched films
    filmList = member.getLetterboxdWatchedFilms()
    f = open(letterboxdPath + "/watchedFilms.txt", "w")
    for film in filmList:
        f.write(film + "\n")
    f.close()
    # Write rated films
    filmList = member.getLetterboxdRatedFilms()
    f = open(letterboxdPath + "/ratedFilms.txt", "w")
    for film in filmList:
        f.write(film + "\n")
    f.close()
    return
