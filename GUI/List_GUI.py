from tkinter import Listbox, Scrollbar, RIGHT, Y, Text, NONE, END, TOP, X
import tkinter


class listGUI:
    def __init__(self, nameList,window):
        top = window


        Lb1 = Listbox(top, height = 300, width = 250, font = ('Arial', 14))


        for x in range(len(nameList)):
            Lb1.insert(x, nameList[x])

        Lb1.pack()
        top.mainloop()

class scrollText:
    def __init__(self, nameList, window):
        root = window


        v = Scrollbar(root)

        v.pack(side= RIGHT, fill = Y)

        t = tkinter.text(root, height = 300, width = 250, wrap = NONE, yscrollcommand = v.set)

        for x in range(len(nameList)):
            t.config(text=nameList[x])



        t.pack(side=TOP, fill = X)

        v.config(command = t.yview)

        root.mainloop()
