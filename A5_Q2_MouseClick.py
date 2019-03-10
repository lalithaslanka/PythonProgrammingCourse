from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Mouse Click Listener")
def leftclick(event):
    messagebox.showinfo("MouseCLICKED","Programmming is Fun")
    print("left")
def middleclick(event):
    messagebox.showinfo("MouseCLICKED","It is fun to Program")
    print("middle")
def rightclick(event):
    messagebox.showinfo("MouseCLICKED","It is really fun to Program")
    print("right")
    
frame = Frame(window, width=300, height=250)
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)
frame.pack()
window.mainloop()
