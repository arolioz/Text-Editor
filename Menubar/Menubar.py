from tkinter import *
from Menubar.MenubarCommands import open

def createMenuBar(window):
    menubar = Menu(window)
    window.config(menu=menubar)

    fileMenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Open",command=lambda:open())
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit)

    editMenu = Menu(menubar,tearoff=0,font=("Arial",10))
    menubar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Cut",command=lambda:print("Cut"))
    editMenu.add_command(label="Copy",command=lambda:print("Copy"))
    editMenu.add_command(label="Paste",command=lambda:print("Paste"))
    editMenu.add_separator()
    editMenu.add_command(label="Customize")