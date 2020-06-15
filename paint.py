"""
Simple paint app using tkinter in python
"""
# imprt library
from tkinter import *
root=Tk()
root.title("Paint App")
root.geometry("500x350")
def display( event ):
    x1,y1=( event.x-3),( event.y-3)
    x2, y2 = (event.x + 3), (event.y + 3)
    color='black'
    w.create_oval(x1,y1,x2,y2,fill=color,outline=color)
w=Canvas(root,width=500,height=350,bg='white')
w.bind( "<b1-motion>",display )
w.pack()
root.mainloop()