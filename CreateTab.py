from tkinter import *
from tkinter import ttk
from Commands import save





def tab(entryText,noteBook):
    frame = Frame(noteBook) #Tab structure
    text = Text(frame)
    text.pack()
    Button(frame,text="Save",command=lambda:save(text)).pack()
    noteBook.add(frame,text=entryText)
    noteBook.pack(expand=True,fill=BOTH)

def createTab(w,noteBook):
    window = Toplevel(w)
 
    entry = Entry(window,font=("Arial",25))
    entry.grid(row=0,column=0)

    creatortButton = Button(window,text="Create",command=lambda:tab(entry.get(),noteBook))
    creatortButton.grid(row=0,column=1)

