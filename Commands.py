from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from Menubar import createMenuBar
from tkinter import colorchooser
from Customization import customize


mainWindow = Tk()
noteBook = ttk.Notebook()
tabs = {}
config = {"Font": "Arial",
          "Font size": 11,
          "Color": "black",
          "Background color": "white"}
            
def save(currentFile):
    file = filedialog.asksaveasfile(initialdir=".\\Files", filetypes=[("Text files", "*.txt"),],defaultextension=".txt")
    if file is None:
        return
    
    fileText = str(currentFile.get(1.0,END))
    
    file.write(fileText)
    file.close()
    
def tab(entryText,noteBook):
    if entryText not in tabs.keys():
        frame = Frame(noteBook) #Tab structure
        frame.pack(expand=True,fill=BOTH)
        text = Text(frame,wrap=WORD)
        text.pack(fill=BOTH,expand=True)
        saveButton = Button(frame,text="Save",command=lambda:save(text), width=15,height=2,relief=GROOVE,bd=4).pack(side=LEFT)
        noteBook.add(frame,text=entryText)
        noteBook.pack(expand=True,fill=BOTH)
        newTabButton = Button(frame,text="New Tab",command=lambda:createTab(),width=15,height=2,relief=GROOVE,bd=4).pack(side=LEFT)
        tabs[entryText] = text
        customizeButton = Button(frame,text="Customize",command=lambda:customize(mainWindow,config,tabs),width=15,height=2,relief=GROOVE,bd=4).pack(side=LEFT)
        setConfig()

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


def setConfig():
    for key,value in tabs.items():
        value.config(font=(config["Font"],config["Font size"]),fg=config["Color"], bg=config["Background color"])
start()