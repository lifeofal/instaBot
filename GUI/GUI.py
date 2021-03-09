import tkinter
import time
import main as instaBot
import List_GUI as lG

def onPressNumber():
    userInput = username.get()
    passInput = password.get()
    print(username)


    initLogin = instaBot.InstaBot('lifeof_alejandro', 'IndiaMike0722!', 'y')
    initFollowers = initLogin.list_creation()
    lG.listGUI(initFollowers,window)


    num.config(text='nothing', justify=tkinter.CENTER, anchor=tkinter.W, wraplength=300)

def resize_window(window):
    window.geometry('600x500')






window = tkinter.Tk()

window.title('iMessage Bot')
window.geometry('600x500')
window.resizable(width=False, height=False)
window.config(background='gray')


title = tkinter.Label(text='instaBot')
title.place(x=100, y=20)
title.config(font=('Times New Roman', 30, 'bold'), background='gray')

numTxt = tkinter.Label(text='Username')
numTxt.place(x=260, y=100)
numTxt.config(font=('Times New Roman', 23, 'bold'), background='gray')

numTxt2 = tkinter.Label(text='Password')
numTxt2.place(x=260, y=200)
numTxt2.config(font=('Times New Roman', 23, 'bold'), background='gray')

username = tkinter.Entry()
username.place(x=255, y=145)
username.config(font=('Times New Roman', 10, 'bold'))

password = tkinter.Entry()
password.place(x=255, y=245)
password.config(font=('Times New Roman', 10, 'bold'))


button = tkinter.Button(text='Confirm', command=onPressNumber)
button.place(x=280, y=425)
button.config(font=100, height=2, width=10)

num = tkinter.Label(text='No message has been sent')
num.place(x=330, y=550, anchor='center')
num.config(font=('Times New Roman', 20, 'bold'), background='gray')

window.mainloop()