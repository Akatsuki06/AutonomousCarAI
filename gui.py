import tkinter as tk
from main import *


root = tk.Tk()
# width x height + x_offset + y_offset:
root.geometry("512*300+30+30")

def train_model():
    pos=get_pos()
    print("training!")
    train(pos)


def test_model():
    pos=get_pos()
    print("testing!")
    drive(pos)

# define and place button
train_btn = tk.Button(root, text='Train',
                      command=train_model)
train_btn.place(x = 20, y = 30, width=120, height=25)
test_btn = tk.Button(root, text='Test',
                     command=test_model)
test_btn.place(x = 20, y = 80, width=120, height=25)
#if dir data has no training data disable it else enable
#test_btn.config(state="disabled")

root.mainloop()
