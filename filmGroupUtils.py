import os
import webScrapeUtils


class FilmGroupMember:
    def __init__(self, name, letterboxdUsername=None):
        self.name = name
        self.letterboxdUsername = letterboxdUsername
        self.letterboxdWatchList = []

    def retrieveLetterboxdWatchList(self):
        if self.letterboxdUsername != None:
            return webScrapeUtils.getLetterboxdWatchlist(self.letterboxdUsername)
        return

    def updateLetterboxdWatchList(self):
        self.letterboxdWatchList = self.retrieveLetterboxdWatchList()
        return

    def getLetterboxdWatchList(self):
        return self.letterboxdWatchList


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
            # TODO add other letterboxd functions once implemented

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
    letterboxdPath = root + "/letterboxd"
    isExist = os.path.exists(letterboxdPath)
    if not isExist:
        os.mkdir(letterboxdPath)
    watchlist = member.getLetterboxdWatchList()
    f = open(letterboxdPath + "/watchlist.txt", "w")
    for film in watchlist:
        f.write(film + "\n")
    f.close()
    return
