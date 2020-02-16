# !/usr/bin/python3
from tkinter import *
import os
import time
root = Tk()
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("720x720+{}+{}".format(positionRight, positionDown))
filename = PhotoImage(file = "cabbarOysh112.png")
canvas = Canvas(root, height = 250, width = 300)
image = canvas.create_image(150, 50, anchor = NE, image = filename)

var1 = 0
def counter():
    global var1
    if var1==9:
        canvas.pack()
    var1 += 1
    var.set(var1)    

var = StringVar()
label = Label( root, textvariable = var, relief = RAISED )  
label.pack()

tupColor = ('fill(255, 204, 0);\n','fill(58, 184, 0);\n','fill(58, 184, 194);\n')
tupImage= ('img = loadImage("images/tiger.jpg");\n','img = loadImage("images/bird.jpg");\n','img = loadImage("images/kitten.jpg");\n','img = loadImage("images/panda.jpg");\n')
def callJava():
    os.chdir("D:/Developer/TheCabbarGithub/raccab-desktop-python")
    os.system("java hello.java")

def callCpp():
    os.chdir("D:/Developer/TheCabbarGithub/raccab-desktop-python")
    os.system("D:/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/g++.exe -g d:/Developer/TheCabbarGithub/raccab-desktop-python/test.cpp -o d:/Developer/TheCabbarGithub/raccab-desktop-python/test.exe")
    time.sleep(2)
    os.system(".\\test.exe")

def callSiSharp():
    os.chdir("D:/Developer/TheCabbarGithub/raccab-desktop-python/MyWinFormsApp")
    os.system("dotnet run")

def callJavaScript():
    global colorJS
    os.chdir("D:/Developer/TheCabbarGithub/raccab-desktop-python")
    with open('p5/sketch.js', 'r') as file:
        data = file.readlines()
    
    if var12.get():
        if data[0] == 'let classifier;\n':
            os.rename('p5/sketch.js', 'p5/sketchml.js')
            time.sleep(1) 
            os.rename('p5/sketchp5.js', 'p5/sketch.js') 
        colorJS=0
        with open('p5/sketch.js', 'r') as file:
            data = file.readlines()
        data[5] = tupColor[colorJS]
    elif var2.get():
        if data[0] == 'let classifier;\n':
            os.rename('p5/sketch.js', 'p5/sketchml.js') 
            time.sleep(1) 
            os.rename('p5/sketchp5.js', 'p5/sketch.js') 
        colorJS=1
        with open('p5/sketch.js', 'r') as file:
            data = file.readlines()
        data[5] = tupColor[colorJS]
    elif var3.get():
        if data[0] == 'let classifier;\n':
            os.rename('p5/sketch.js', 'p5/sketchml.js')
            time.sleep(1)             
            os.rename('p5/sketchp5.js', 'p5/sketch.js') 
        colorJS=2
        with open('p5/sketch.js', 'r') as file:
            data = file.readlines()
        data[5] = tupColor[colorJS]
    elif var123.get():
        if data[0] == 'function setup() {\n':
            os.rename('p5/sketch.js', 'p5/sketchp5.js')
            time.sleep(1) 
            os.rename('p5/sketchml.js', 'p5/sketch.js') 
        colorJS=0
        with open('p5/sketch.js', 'r') as file:
            data = file.readlines()
        data[7] = tupImage[colorJS]
    elif var23.get():
        if data[0] == 'function setup() {\n':
            os.rename('p5/sketch.js', 'p5/sketchp5.js')
            time.sleep(1) 
            os.rename('p5/sketchml.js', 'p5/sketch.js') 
        colorJS=1
        with open('p5/sketch.js', 'r') as file:
            data = file.readlines()
        data[7] = tupImage[colorJS]
    elif var33.get():
        if data[0] == 'function setup() {\n':
            os.rename('p5/sketch.js', 'p5/sketchp5.js')
            time.sleep(1) 
            os.rename('p5/sketchml.js', 'p5/sketch.js') 
        colorJS=2
        with open('p5/sketch.js', 'r') as file:
            data = file.readlines()
        data[7] = tupImage[colorJS]
    elif var333.get():
        if data[0] == 'function setup() {\n':
            os.rename('p5/sketch.js', 'p5/sketchp5.js')
            time.sleep(1) 
            os.rename('p5/sketchml.js', 'p5/sketch.js') 
        colorJS=3
        with open('p5/sketch.js', 'r') as file:
            data = file.readlines()
        data[7] = tupImage[colorJS]
    
    with open('p5/sketch.js', 'w') as file:
        file.writelines( data )

def callUnity():
    os.chdir("D:/Developer/TheCabbarGithub/raccab-desktop-python")
    os.system(".\\Unity\PythonTest.exe")

def callHTML():
    os.chdir("D:/Developer/TheCabbarGithub/raccab-desktop-python")
    with open('html/index.html', 'r') as file:
        data = file.readlines()
        with open('html/index.html', 'r') as file:
            data = file.readlines()
        a = qq3q34.get()
        data[8] = a
    with open('html/index.html', 'w') as file:
        file.writelines( data )

B = Button(root, text = "Increment", command = counter)
B.pack()
a = Button(root, text = "YASOMONT JAVA PROGRAM MUHTESEM", command = callJava)
a.pack()
ss = Button(root, text = "YASOMONT C# PROGRAM MUHTESEM", command = callSiSharp)
ss.pack()
sss = Button(root, text = "ARMY FABRIKASI C++ PROGRAMI MUHTESEM", command = callCpp)
sss.pack()

var12 = IntVar()
q=Checkbutton(root, text="yellow", variable=var12)
q.pack()
var2 = IntVar()
qq=Checkbutton(root, text="green", variable=var2)
qq.pack()
var3 = IntVar()
qqq=Checkbutton(root, text="blue", variable=var3)
qqq.pack()

var123 = IntVar()
q3=Checkbutton(root, text="tiger", variable=var123)
q3.pack()
var23 = IntVar()
qq3=Checkbutton(root, text="bird", variable=var23)
qq3.pack()
var33 = IntVar()
qq3q=Checkbutton(root, text="kitten", variable=var33)
qq3q.pack()
var333 = IntVar()
qq3q3=Checkbutton(root, text="panda", variable=var333)
qq3q3.pack()

colorJS=0

ssss = Button(root, text = "ARMY FABRIKASI Javascript PROGRAMI MUHTESEM", command = callJavaScript)
ssss.pack()

ssssa = Button(root, text = "MAHONYL MMORPG Unity PROGRAMI MUHTESEM", command = callUnity)
ssssa.pack()

with open('html/index.html', 'r') as file:
    data = file.readlines()
qq3q34=Entry(root,width=100)
qq3q34.insert(0,data[8])
qq3q34.pack()

ssssas = Button(root, text = "KAMIL YEDEK html PROGRAMI MUHTESEM", command = callHTML)
ssssas.pack()


dd = Button(root, text='Quit', command=root.quit)
dd.pack()
root.title("Simple Prog")
root.mainloop()
