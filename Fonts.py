from tkinter import *
from tkinter import font




    
def setFont(w,config,label,tabs):
    root = Toplevel(w)
    frame = Frame(root,bg="lightyellow",bd=2,)
    frame.pack()
    root.title("Font")
    Label(frame,text="Font name",font=("Arial",15),bg="lightyellow").pack(side=TOP)
    def setConfig():
        if entry.get() in font.families():
            config["Font"] = entry.get()
            label.config(font=(config["Font"],config["Font size"]))
            for key,value in tabs.items():
                value.config(font=(config["Font"],config["Font size"]),fg=config["Color"], bg=config["Background color"])
    entry = Entry(frame,font=("Arial",25))
    entry.pack(side=LEFT)

    creatortButton = Button(frame,text="Submit",command=lambda:setConfig())
    creatortButton.pack(side=RIGHT)
    

