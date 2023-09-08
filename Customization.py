from tkinter import *
from tkinter import colorchooser
from Fonts import setFont


def customize(w,config,tabs):
    cust_window = Toplevel(w)
    cust_window.title("Customize")
    cust_window.geometry("320x80")
    frame = Frame(cust_window,bd=2,relief=GROOVE,bg="lightyellow")
    frame.pack(fill=BOTH)
    label = Label(frame,text="Sample",width=15,height=2,bg="lightyellow")
    label.pack(side=TOP)
    config = config
    tabs = tabs
    def set(x):
        if x == 1:
            textColor = colorchooser.askcolor()
            config["Color"] = textColor[1]
            label.config(fg=config["Color"])
        elif x == 2:
            bgColor = colorchooser.askcolor()
            config["Background color"] = bgColor[1]
            label.config(bg=bgColor[1])
        elif x == 3:
            config["Font size"] = scale.get()
            label.config(font=(config["Font"],config["Font size"]))
        elif x == 4:
            setFont(cust_window,config,label,tabs)
        setConfig(tabs,config)
    colorButton = Button(frame,text="Text Color",command=lambda:set(1)).pack(side=LEFT)
    bgButton = Button(frame,text="Bg Color",command=lambda:set(2)).pack(side=LEFT)
    scale = Scale(frame,from_=0,to=16,length=100,orient=HORIZONTAL,font=("Arial",10,"bold"),troughcolor="grey",resolution=1,fg="black",showvalue=2)
    scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"])
    scale.pack(side=LEFT)
    sizeButton = Button(frame,text="✅",command=lambda:set(3), padx=5,bg="lightgreen").pack(side=LEFT)
    fontsButton = Button(frame,text="Fonts",command=lambda:set(4), padx=5,bg="lightyellow").pack(side=RIGHT)

def setConfig(tabs,config):
    for key,value in tabs.items():
        value.config(font=(config["Font"],config["Font size"]),fg=config["Color"], bg=config["Background color"])