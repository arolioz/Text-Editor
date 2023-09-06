from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from Menubar import createMenuBar

mainWindow = Tk()
noteBook = ttk.Notebook()


def save(currentFile):
    file = filedialog.asksaveasfile(initialdir=".\\Files", filetypes=[("Text files", "*.txt"),],defaultextension=".txt")
    if file is None:
        return
    
    fileText = str(currentFile.get(1.0,END))
    
    file.write(fileText)
    file.close()
    
def tab(entryText,noteBook):
    frame = Frame(noteBook) #Tab structure
    text = Text(frame,width=150,height=30)
    text.pack()
    saveButton = Button(frame,text="Save",command=lambda:save(text)).pack(side=TOP)
    noteBook.add(frame,text=entryText)
    noteBook.pack(expand=True,fill=BOTH)
    newTabButton = Button(frame,text="New Tab",command=lambda:createTab()).pack(side=TOP)
   

def createTab():
    window = Toplevel(mainWindow)
 
    entry = Entry(window,font=("Arial",25))
    entry.grid(row=0,column=0)

    creatortButton = Button(window,text="Create",command=lambda:tab(entry.get(),noteBook))
    creatortButton.grid(row=0,column=1)

def start():
    tab("Tab",noteBook)
    createMenuBar(mainWindow)
    mainWindow.mainloop()

