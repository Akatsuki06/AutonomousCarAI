
# coding: utf-8

# In[1]:


import keyboard


# In[2]:


def left():
    keyboard.press('a')
    keyboard.release('w')
    keyboard.release('s')
    keyboard.release('d')

def right():
    keyboard.press('d')
    keyboard.release('w')
    keyboard.release('s')
    keyboard.release('a')

def accelerate():
    keyboard.press('w')
    keyboard.release('d')
    keyboard.release('s')
    keyboard.release('a')   
    
def deaccelerate():
    keyboard.press('d')
    keyboard.release('w')
    keyboard.release('s')
    keyboard.release('a')

