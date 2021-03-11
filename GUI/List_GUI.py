from tkinter import Listbox

class listGUI:
    def __init__(self, nameList,window):
        top = window


        Lb1 = Listbox(top, height = 300, width = 250, font = ('Arial', 14))


        for x in range(len(nameList)):
            Lb1.insert(x, nameList[x])

        Lb1.pack()
        top.mainloop()