from tkinter import *
from Structure.Commands import start,mainWindow
from Menubar.Menubar import createMenuBar


def Main():
    createMenuBar(mainWindow)
    start()
    
if __name__ == "__main__":
    Main()