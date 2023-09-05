from tkinter import *
from Menubar import createMenuBar
from CreateTab import createTab,tab
from tkinter import ttk


mainWindow = Tk()

def Main():
    noteBook = ttk.Notebook()
    tab("Tab",noteBook)
    noteBook = ttk.Notebook()
    createMenuBar(mainWindow)
    
    mainWindow.mainloop()
    
if __name__ == "__main__":
    Main()

