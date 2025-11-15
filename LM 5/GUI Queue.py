import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x700")

class Queue:
    def __init__(self):
        self.element = []

    def enqueue (self):
        x = b2_answer.get(1.0, "end-1c")
        self.element.append(x)
        b2_answer.delete(1.0, END)

    def dequeue (self):
        self.element.pop(0)

    def displayQueue (self):
        for i in self.element:
            b4_display.insert(tk.INSERT, i+"  ")



## Main Code

q1 = Queue()

b2 = Button(top, text="Add to Queue", width=15, height=5, command = lambda: q1.enqueue())
b2.place(x=100, y=150) ## Need a Text box to add something

b2_answer = Text(width=25, height=2)
b2_answer.place(x = 250, y=150)

b3 = Button(top, text="Remove Queue", width=15, height=5, command= lambda: q1.dequeue())
b3.place(x=100, y=250) ## No text box

b4 = Button(top, text="Display Queue", width=15, height=5, command = lambda: q1.displayQueue())
b4.place(x=100, y=350) ## Need a Textbox to display

b4_display = tk.Entry(top,width=30)
b4_display.place(x=250, y=350)

b5 = Button(top, text="Delete Display", width=15, height=5, command=lambda: b4_display.delete(0,END))
b5.place(x=100, y=450)

top.mainloop()

