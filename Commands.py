from tkinter import *
from tkinter import filedialog

def save(currentFile):
    file = filedialog.asksaveasfile(initialdir=".\\Files", filetypes=[("Text files", "*.txt"),],defaultextension=".txt")
    if file is None:
        return
    
    fileText = str(currentFile.get(1.0,END))
    
    file.write(fileText)
    file.close()
    
