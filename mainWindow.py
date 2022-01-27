from tkinter import *
import tkinter
from tkinter import ttk

import filmGroupUtils


def addNewGroupToList(groupList, newGroupName):
    gl = groupList.append(filmGroupUtils.filmGroup(newGroupName))
    filmGroupList = gl

mm = filmGroupUtils.filmGroup("Movie Mondays")
group2 =filmGroupUtils.filmGroup("Family Movie Group")
filmGroupList = []

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