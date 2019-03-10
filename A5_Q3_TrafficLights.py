from tkinter import *

window = Tk()
window.title("Traffic Lights System")

frame1 = Frame(window)
frame1.pack(expand=1, fill=X)
#CREATE CANVAS  TO DRAW TRAFFIC LIGHTS
w= Canvas(frame1,width = 300, height = 500)
w.pack()
#traffic lights
w.create_rectangle(100,100,200,400)
green_light = w.create_oval(100,100,200,200)
yellow_light = w.create_oval(100,200,200,300)
red_light = w.create_oval(100,300,200,400)

def change_color():
    selection = var.get()
    if selection == 1:
        w.itemconfig(green_light, fill= "green")
        w.itemconfig(yellow_light, fill= "white")
        w.itemconfig(red_light, fill= "white")
    elif selection ==2:
        w.itemconfig(green_light, fill= "white")
        w.itemconfig(yellow_light, fill= "yellow")
        w.itemconfig(red_light, fill= "white")
    elif selection == 3:
        w.itemconfig(green_light, fill= "white")
        w.itemconfig(yellow_light, fill= "white")
        w.itemconfig(red_light, fill= "red")
    
#radio button

#creating another frame for radiobutton
frame2 = Frame(window)
frame2.pack()
var = IntVar()
Radiobutton(frame2, text = "Green", variable = var,command = change_color, value = 1).grid(row=0, column=0, sticky = W)
Radiobutton(frame2, text = "Yellow", variable = var,command = change_color, value = 2).grid(row=0, column=1, sticky = W)
Radiobutton(frame2, text = "Red", variable = var,command = change_color, value = 3).grid(row=0, column=2, sticky = W)

window.mainloop()
                
