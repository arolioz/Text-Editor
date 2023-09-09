from tkinter import *
from tkinter import font

def setFont(w,config,label,tabs):
    root = Toplevel(w)
    root.config(bg="lightyellow")
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
    entry = Entry(frame,font=("Arial",15))
    entry.pack(side=LEFT)
    listbox = Listbox(root)
    listbox.pack(side = LEFT, fill = BOTH)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side = LEFT, fill = BOTH)
    for values in font.families():
        listbox.insert(END, values)
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)

    creatortButton = Button(frame,text="Submit",command=lambda:setConfig())
    creatortButton.pack(side=RIGHT)
    applyButton = Button(root,text="Apply",command=lambda:set()).pack(side=LEFT)
    
    def set():
        entry.delete(0,END)
        entry.insert(0,listbox.selection_get())
        entry.config(font=(listbox.selection_get(),15))