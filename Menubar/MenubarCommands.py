from tkinter import *
from Structure.Commands import tab,noteBook,tabs
from tkinter import filedialog

def open():
    f = filedialog.askopenfile(initialdir="Files")
    fileName = f.name
    
    #Gets the name of the file
    file_path_components = fileName.split('/')
    file_name_and_extension = file_path_components[-1].rsplit('.', 1)

    #Creates a tab and write the content from the selected file
    tab(file_name_and_extension[0],noteBook)
    t = tabs.get(file_name_and_extension[0])
    t.insert(1.0,f.read())