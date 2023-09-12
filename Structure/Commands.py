from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import colorchooser
from Customization.Customization import customize


#Main window 
mainWindow = Tk()
mainWindow.title("Text editor")
#Logo
mainWindow.iconphoto(True,PhotoImage(file="Assets\\MainIcon.png"))

#Main notebook
noteBook = ttk.Notebook()

#Stores all existing text areas from the tabs 
tabs = {}
#Text area configuration
config = {"Font": "Arial",
          "Font size": 11,
          "Color": "black",
          "Background color": "white"}
            
def save(currentFile):
    #Save the file and insert the text within the text area
    file = filedialog.asksaveasfile(initialdir=".\\Files", filetypes=[("Text files", "*.txt"),],defaultextension=".txt")
    if file is None:
        return
    fileText = str(currentFile.get(1.0,END))
    
    file.write(fileText)
    file.close()
    
def tab(entryText,noteBook):
    #Checks if theres already a tab with the given name 
    if entryText not in tabs.keys():
        #Main frame 
        frame = Frame(noteBook) #Tab structure
        frame.pack(expand=True,fill=BOTH)
        #Text area
        text = Text(frame,wrap=WORD)
        text.pack(fill=BOTH,expand=True)

        #Save button
        saveButton = Button(frame,text="Save",command=lambda:save(text), width=15,height=2,relief=GROOVE,bd=4).pack(side=LEFT)

        #Adds the frame to the tab
        noteBook.add(frame,text=entryText)
        noteBook.pack(expand=True,fill=BOTH)

        #Button to create a new tab
        newTabButton = Button(frame,text="New Tab",command=lambda:createTab(),width=15,height=2,relief=GROOVE,bd=4).pack(side=LEFT)
        #Adds the created tab to the tabs dic 
        tabs[entryText] = text
        customizeButton = Button(frame,text="Customize",command=lambda:customize(mainWindow,config,tabs),width=15,height=2,relief=GROOVE,bd=4).pack(side=LEFT)
        #Apply the configuration so u dont have to change it again 
        setConfig()

def createTab():
    window = Toplevel(mainWindow)
    window.title("Create tab")
    entry = Entry(window,font=("Arial",25))
    entry.grid(row=0,column=0)

    #creates a new tab and adds it to the main window
    creatortButton = Button(window,text="Create",command=lambda:tab(entry.get(),noteBook))
    creatortButton.grid(row=0,column=1)

def start():
    #Default tab
    tab("Tab",noteBook)
    
    mainWindow.mainloop()


def setConfig():
    #Loops thru every tab in the dic and apply the configuration from the configuration dic
    for key,value in tabs.items():
        value.config(font=(config["Font"],config["Font size"]),fg=config["Color"], bg=config["Background color"])
