class filmGroupMember:
    def __init__(self, name, letterboxdUsername=None):
        self.name = name
        self.letterboxdUsername = letterboxdUsername


class filmGroup:
    def __init__(self, groupName, members=None):
        self.groupName = groupName
        self.members = members

    def addMember(self, newMember):
        if newMember in self.members:
            return
        self.members.apend(newMember)

    def removeMember(self, memberToRemove):
        if memberToRemove in self.members:
            self.members.remove(memberToRemove)
        return

    def getMembers(self):
        return self.members

    def __str__(self):
        return self.groupName