import tkinter as tk
from main import *

pos = None
def get_game_position():
    pos=get_position(pag)
    if pos==None:
        print('loading cached frame location ...')
        f=open('data/frames-pos.temp','r')
        pos=eval(f.read())
        f.close()
    else:
        f=open('data/frames-pos.temp','w')
        f.write(str(pos))
        f.close()

    print('Frames will be captured at : ', pos)

get_game_position()

root = tk.Tk()
# width x height + x_offset + y_offset:
root.geometry("170x130+30+30")

def train_model():
    print("click!")
    test_btn.config(state="disabled")
    train_btn.config(state="disabled")

    # do the training
    train(pos)

    test_btn.config(state="enabled")
    train_btn.config(state="enabled")


def test_model():
    print("clicked!")
    train_btn.config(state="disabled")
    test_btn.config(state="disabled")

    # do the testing
    test(pos)

    test_btn.config(state="enabled")
    train_btn.config(state="enabled")

# define and place button
train_btn = tk.Button(root, text='Train',
                      command=train_model)
train_btn.place(x = 20, y = 30, width=120, height=25)
test_btn = tk.Button(root, text='Test',
                     command=test_model)
test_btn.place(x = 20, y = 80, width=120, height=25)
test_btn.config(state="disabled")

root.mainloop()
