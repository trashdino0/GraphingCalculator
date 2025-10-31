#graphing calculator 
import turtle as trtl
import math
import tkinter as tk
from functools import partial
import random

def drawGraphLines(bottomLeftX,bottomLeftY,upperRightX,upperRightY):

    grapher.pencolor('black')
    grapher.pensize(1)
    wn.colormode(255)

    wn.setworldcoordinates(bottomLeftX,bottomLeftY,upperRightX,upperRightY)
    wn.tracer(0)

    grapher.penup()
    grapher.goto(bottomLeftX,bottomLeftY+(upperRightY-bottomLeftY)/2)
    grapher.pendown()
    grapher.goto(upperRightX,bottomLeftY+(upperRightY-bottomLeftY)/2)
    grapher.penup()

    grapher.goto(bottomLeftX+(upperRightX-bottomLeftX)/2,bottomLeftY)
    grapher.pendown()
    grapher.goto(bottomLeftX+(upperRightX-bottomLeftX)/2,upperRightY)

    grapher.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    grapher.pensize(3)
    grapher.penup()

    exitButton.pack()
    exitButton.place(x=600,y=10)  #places button on screen

    restartButton.pack()
    restartButton.place(x=550,y=10)

    addButton.pack()
    addButton.place(x=515,y=10)

def exitCommand():
    wn.bye()
    root.destroy()

def restartGraph():
    wn.resetscreen()
    grapher.reset()
    root.deiconify()

def addGraph():
    root.deiconify()

def setVarAndShowGraph(whichFunction):

    varA = inpData1.get() if inpData1.get() != '' else 0
    varB = inpData2.get() if inpData2.get() != '' else 0
    varC = inpData3.get() if inpData3.get() != '' else 0
    varD = inpData4.get() if inpData4.get() != '' else 0

    winFrame.tkraise()
    winRoot.destroy()

    match whichFunction.lower():
        case 'sin'|'cos'|'tan':
            graphSCT(whichFunction, float(varA), float(varB), float(varC),float(varD))
        case 'slope':
            graphSlope(float(varA), float(varB))
        case 'log':
            graphLog(float(varA))
        case _:
            graphQuadratic(float(varA), float(varB), float(varC))

def getInputs(whichEq, winHead, inpLabels):
    global winRoot, winFrame, labelChoice, entButton, inpTxt1, inpTxt2, inpTxt3, inpTxt4, inpData1, inpData2, inpData3, inpData4

    winRoot = tk.Tk()
    winRoot.wm_geometry("280x250")
    winRoot.title('Getting Input')

    winFrame = tk.Frame(winRoot)
    winFrame.grid(row=0, column=0, sticky='news')

    labelChoice = tk.Label(winFrame, text=winHead)
    labelChoice.pack()

    #Create input entries and pack only whats needed
    inpData1 = tk.Entry(winFrame, bd=3)
    inpData2 = tk.Entry(winFrame, bd=3)    
    inpData3 = tk.Entry(winFrame, bd=3)
    inpData4 = tk.Entry(winFrame, bd=3)

    if whichEq == 'Sin' or whichEq == 'Cos' or whichEq == 'Tan':
        inpTxt1 = tk.Label(winFrame, text=inpLabels[0]).pack(padx=60)
        inpData1.pack(padx=60)
        inpTxt2 = tk.Label(winFrame, text=inpLabels[1]).pack(padx=60)
        inpData2.pack(padx=60)
        inpTxt3 = tk.Label(winFrame, text=inpLabels[2]).pack(padx=60)
        inpData3.pack(padx=60)
        inpTxt4 = tk.Label(winFrame, text=inpLabels[3]).pack(padx=60)
        inpData4.pack(padx=60)
    elif whichEq == 'Slope':
        inpTxt1 = tk.Label(winFrame, text=inpLabels[0]).pack(padx=60)
        inpData1.pack(padx=60)
        inpTxt2 = tk.Label(winFrame, text=inpLabels[1]).pack(padx=60)
        inpData2.pack(padx=60)
    elif whichEq == 'Quadratics':
        inpTxt1 = tk.Label(winFrame, text=inpLabels[0]).pack(padx=60)
        inpData1.pack(padx=60)
        inpTxt2 = tk.Label(winFrame, text=inpLabels[1]).pack(padx=60)
        inpData2.pack(padx=60)
        inpTxt3 = tk.Label(winFrame, text=inpLabels[2]).pack(padx=60)
        inpData3.pack(padx=60)       
    elif whichEq == 'Log':
        inpTxt1 = tk.Label(winFrame, text=inpLabels[0]).pack(padx=60)
        inpData1.pack(padx=60)

    entButton = tk.Button(winFrame, text='Enter', command=partial(setVarAndShowGraph,whichEq)).pack()

    winFrame.tkraise()
    winRoot.mainloop()

def whenClicked():
    
    choice = menu.get()
    root.withdraw()

    match choice:
        case 'Sin':
            getInputs(choice, 'Graphing y = a * sin(fx - h) + v', ['Value for amplitude', 'Value for frequency', 'Value for vertical phase', 'Value for horizontal phase'])
        case 'Cos':
            getInputs(choice, 'Graphing y = a * cos(fx - h) + v', ['Value for amplitude', 'Value for frequency', 'Value for vertical phase', 'Value for horizontal phase'])
        case 'Tan':
            getInputs(choice, 'Graphing y = a * tan(fx - h) + v', ['Value for amplitude', 'Value for frequency', 'Value for vertical phase', 'Value for horizontal phase'])
        case 'Log':
            getInputs(choice, 'Graphing Log(x)', ['Value for X'])       
        case 'Slope':
            getInputs(choice, 'Graphing y = mx + b', ['Value for m', 'Value for b'])
        case 'Quadratics':
            getInputs(choice, 'Graphing y = ax^2 + bx + c', ['Value for a','Value for b','Value for c'])
            
def graphSCT(whichFunc, amp, frequency, phaseV, phaseH):

    xval = -1000.0
    yval = 0

    drawGraphLines(-1000,-1000,1000,1000)

    match whichFunc.lower():
        case 'tan':
            yval = ((amp)*10 * math.tan(2.0 * math.pi * frequency * (xval/2000.0) - phaseH) + phaseV)
        case 'cos':
            yval = ((amp)*10 * math.cos(2.0 * math.pi * frequency * (xval/2000.0) - phaseH) + phaseV)
        case 'sin':
            yval = ((amp)*10 * math.sin(2.0 * math.pi * frequency * (xval/2000.0) - phaseH) + phaseV)
    
    grapher.goto(-1000,yval)
    grapher.pendown()

    while xval <= 1000:
        match whichFunc.lower():
            case 'tan':
                yval = ((amp)*10 * math.tan(2.0 * math.pi * frequency * (xval/2000.0) + phaseH) + phaseV)
            case 'cos':
                yval = ((amp)*10 * math.cos(2.0 * math.pi * frequency * (xval/2000.0) + phaseH) + phaseV)
            case 'sin':
                yval = ((amp)*10 * math.sin(2.0 * math.pi * frequency * (xval/2000.0) + phaseH) + phaseV)

        grapher.goto(xval,yval)
        xval += 1
        wn.update()

def graphLog(logVal):

    drawGraphLines(-1000,-1000,1000,1000)

    counter = 1
    yval = 1

    grapher.penup()

    yval = math.log(counter)
    grapher.goto(counter, yval * logVal)
    grapher.pendown()

    while counter <= 1000:
        counter = counter + 1
        yval = math.log(counter)
        grapher.goto(counter, yval * logVal)
        wn.update()

def graphQuadratic(a,b,c):

    drawGraphLines(-1000,-1000,1000,1000)

    for x in range(-6000,6000):
        yval = ((a*(x**2)+(b*x)+c)/100)
        grapher.goto(x,yval)
        wn.update()
        grapher.pendown()

def graphSlope(m,b):

    drawGraphLines(-1000,-1000,1000,1000)

    grapher.penup()
    grapher.goto(-6000,(m*(-6000)+b))
    grapher.pendown()

    for x in range(-6000,6000):
        yval = ((m*x+b))
        grapher.goto(x,yval)
        wn.update() 

#Starts the entire program
root = tk.Tk()
root.title('Graphing Calculator')
root.geometry('280x250')

menu=tk.StringVar()
menu.set('Quadratics')

options = ['Quadratics', 'Slope', 'Sin', 'Cos', 'Tan', 'Log']

dropMenu = tk.OptionMenu(root, menu, *options)
dropMenu.pack()

button = tk.Button(root, text='Submit', command=whenClicked).pack()

wn = trtl.Screen()

grapher = trtl.Turtle()
grapher.speed('fastest')

turtleScreen = wn.getcanvas()
exitButton = tk.Button(turtleScreen.master, text="Exit", command=exitCommand)
restartButton = tk.Button(turtleScreen.master, text="Restart", command=restartGraph)
addButton = tk.Button(turtleScreen.master, text="Add", command=addGraph)

root.mainloop() 