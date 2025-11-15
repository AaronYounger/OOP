import tkinter as tk
from tkinter import *


top = Tk()
top.geometry("500x700")

class Stacks:
    def __init__(self):
        self.element = []
    def push(self):
        x = push_answer.get(1.0, "end-1c")
        self.element.append(x)
        push_answer.delete(1.0, END)
    def pop(self):
        self.element.pop()

    def displaystack(self):
        for i in self.element:
            display_text.insert(tk.INSERT, i+"  ")



## Main Code
s1 = Stacks()

push_button = Button(top, text="Add to Stack", width=20, height=5, command= lambda: s1.push())
push_button.place(x=75, y=100)

push_answer = Text(width=25, height=2)
push_answer.place(x=250, y=100)

pop_button = Button(top, text="Remove from Stack", width=20, height=5, command=lambda: s1.pop())
pop_button.place(x=75, y=200)

display_button = Button(top, text="Display Stack", width=20, height=5, command=lambda: s1.displaystack())
display_button.place(x=75, y=300)

display_text = tk.Entry(top, width=30)
display_text.place(x=250,y=325)

delete_display = Button(top, text="Delete Display", width=20, height=5, command=lambda: display_text.delete(0, END))
delete_display.place(x=75, y=400)

top.mainloop()
