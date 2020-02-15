# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

root = Tk()
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("360x360+{}+{}".format(positionRight, positionDown))

var1 = 0
def counter():
    global var1    
    var1 += 1
    var.set(var1)    

var = StringVar()
label = Label( root, textvariable = var, relief = RAISED )  
label.pack()

B = Button(root, text = "Increment", command = counter)
B.pack()

root.title("Simple Prog")
root.mainloop()