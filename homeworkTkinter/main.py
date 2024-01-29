from tkinter import *

def packageComponents(*components):
    for component in components:
        component.pack()
def configButtons(*buttons):
    colors = ["red", "blue", "green", "yellow", "pink", "purple", "magenta", "orange", "brown", "aqua"]
    btnIndex = 0
    for button in buttons:
        button.config(text=colors[btnIndex].capitalize(), bg=colors[btnIndex])
        btnIndex += 1
def configLabels(*labels):
    hexColors = ["#ff0000", "#0000ff", "#008000", "#ffff00", "#ffc0cb", "#800080", "#ff00ff", "#ffa500", "#a52a2a", "#00ffff"]
    labelIndex = 0
    for labelObj in labels:
        labelObj.config(text=hexColors[labelIndex])
        labelIndex += 1

root = Tk()

root.geometry("200x550")
root.resizable(False, False)
root.title("Color picker")

btn1 = Button()
btn2 = Button()
btn3 = Button()
btn4 = Button()
btn5 = Button()
btn6 = Button()
btn7 = Button()
btn8 = Button()
btn9 = Button()
btn10 = Button()

lab1 = Label()
lab2 = Label()
lab3 = Label()
lab4 = Label()
lab5 = Label()
lab6 = Label()
lab7 = Label()
lab8 = Label()
lab9 = Label()
lab10 = Label()

configButtons(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
configLabels(lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9, lab10)
packageComponents(btn1, lab1, btn2, lab2, btn3, lab3, btn4, lab4, btn5, lab5, btn6, lab6, btn7, lab7, btn8, lab8, btn9, lab9, btn10, lab10)

root.mainloop()
