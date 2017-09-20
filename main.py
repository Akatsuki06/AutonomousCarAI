
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pyautogui as pag
import cv2
import pyscreenshot as ImageGrab
import time
import keyboard 
import pickle
import win32gui, win32ui, win32con, win32api
from lib.game_position import get_position,get_screen
from lib.process_image import process_img
from lib.capture_keys import log_keys,get_keys
# from lib.directions import left,right,accelerate,deaccelerate


# In[2]:




def train():
    for i in range(1,4):
        print(i ,'seconds')
        time.sleep(1)
    print('training...')
    fps=0
    training_frames=pd.DataFrame()
    training_keys=pd.DataFrame()
    while True:
        t=time.time()
        intsarray,height,width=get_screen(pos,win32gui, win32ui, win32con, win32api)
        img=process_img(intsarray,height,width,np,cv2)        
        fps+=time.time()-t
        key = get_keys(win32api)
        training_frames=training_frames.append([img.flatten()])
        training_keys= training_keys.append([key])
        print(';',end='')
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break;
    print('\nfps: ',fps/len(training_frames),'trained-frames: ', len(training_frames),len(training_keys))
    training_frames=training_frames[10:len(training_frames)-10]
    training_keys=training_keys[10:len(training_keys)-10]
    training_frames.to_csv('training_frames.csv',index=False)
    training_keys.to_csv('training_keys.csv',index=False,header=['w','s','a','d'])#remove nk


# In[ ]:





# In[3]:


def getmax(y):
    max=0
    for i in range(0,len(y)):
        if(y[i]>y[max]):max=i
    arr=['w','s','a','d']
    return arr[i]
    

def drive(model):
    
    for i in range(1,4):
        print(i ,'seconds')
        time.sleep(1)
    k=cv2.waitKey(1)
    while True:
        intsarray,height,width=get_screen(pos,win32gui, win32ui, win32con, win32api)
        img=process_img(intsarray,height,width,np,cv2)
        X=img.reshape((img.shape[0],30,30,1))
        X=X.astype('float')
        X/=255
        y=model.predict(X)
        #predict handle the game
        y=y.flatten()
        print(getmax(y))
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break;


# In[4]:



pos=get_position(pag)
print('frames will be captured at',pos)
if pos==None:
    pos=(843, 39, 512, 384)


# In[5]:


# inp=input('train or test?')
# inp="train"
# if(inp=="train"):
train()
# from keras.models import load_model
# model=load_model('model1.h5')
# drive(model)


# In[6]:


# df=pd.read_csv('data1/training_keys.csv')
# df.shape
# df[df['nk']>0].count()


# In[7]:


# from keras.models import load_model
# model=load_model('model.h5')
# drive(model)


# In[ ]:




