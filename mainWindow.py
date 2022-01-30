from tkinter import *
import tkinter
from tkinter import ttk

import filmGroupUtils


def addNewGroupToList(groupList, newGroupName):
    gl = groupList.append(filmGroupUtils.FilmGroup(newGroupName))
    filmGroupList = gl

movieMondays = filmGroupUtils.FilmGroup("Movie Mondays")
filmGroupList = []

#["baudehlaire","kalekdan","ayfex","jamesiam","aliiim"]
joe = filmGroupUtils.FilmGroupMember("Joe","kalekdan")
james = filmGroupUtils.FilmGroupMember("James","jamesiam")
ali = filmGroupUtils.FilmGroupMember("Ali","aliiim")
alicia = filmGroupUtils.FilmGroupMember("Alicia","ayfex")
sofia = filmGroupUtils.FilmGroupMember("Sofia","baudehlaire")

movieMondays.addMembers([joe, james, ali, alicia, sofia])
movieMondays.updateMembersLetterboxd()
movieMondays.saveFilmGroup()
#filmGroupUtils.loadFilmGroup("Movie Mondays")

root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
groupNameEntry = ttk.Entry(frm)
groupNameEntry.grid(column=0, row=0)
groupComboBox = ttk.Combobox(frm, values=filmGroupList).grid(column=0, row=1)
ttk.Button(frm, text="Create new group", command=lambda: addNewGroupToList(filmGroupList, groupNameEntry.get())).grid(column=1, row=0)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
# ttk.Button(frm, text="aw", command=lambda: printtext("4")).grid(column=2, row=0)


root.mainloop()