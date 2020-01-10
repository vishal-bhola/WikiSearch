import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

win = Tk()
win.title('Wikipedia')
win.geometry('500x150')

def search_wiki():
    search = entry.get()
    answer = wikipedia.summary(search)
    showinfo("Wikipedia Answer",answer)


label = Label(win,text="Wikipedia Search :")
label.grid(row=1, column=2)

entry = Entry(win,width=25)
entry.grid(row=3, column=6)

button = Button(win,text="Search",command=search_wiki)
button.grid(row=7,column=6,padx=10)


win.mainloop()
