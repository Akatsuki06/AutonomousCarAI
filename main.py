import numpy as np
import pandas as pd
import pyautogui as pag
import cv2
import pyscreenshot as ImageGrab
import time
import keyboard 
import win32gui, win32ui, win32con, win32api
from lib.game_position import get_position,get_screen
from lib.process_image import process_img
from lib.capture_keys import log_keys,get_keys
from lib.directions import left,right,accelerate,deaccelerate
import glob
from keras.models import load_model


def train(pos):
    findex=len(glob.glob('data/*frames*.csv'))+1
    filename_frames='data/trainig_frames-'+str(findex)+'.csv'
    filename_keys='data/training_keys-'+str(findex)+'.csv'
    for i in range(1,4):
        print(i ,'')
        time.sleep(1)
    print('writing to ' , filename_frames,' and ', filename_keys, ' ....')
    print('training now...(press Q to stop)')
    fps=0
    training_frames=pd.DataFrame()
    training_keys=pd.DataFrame()
    while True:
        t=time.time()
        intsarray,height,width=get_screen(pos,win32gui, win32ui, win32con, win32api)
        img=process_img(intsarray,height,width,np,cv2)     
        cv2.imshow('Training',img)
        img=img.flatten()
        fps+=time.time()-t
        key = get_keys(win32api)
        if key==0:
            cv2.destroyAllWindows()
            break;
        training_frames=training_frames.append([img])
        training_keys= training_keys.append([key])
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break;
    print('\nfps: ',len(training_frames)/fps)
    print('no of frames trained: ', len(training_frames))
    #discarding some of the frames
    training_frames=training_frames[10:len(training_frames)-10]
    training_keys=training_keys[10:len(training_keys)-10]
    training_frames.to_csv(filename_frames,index=False)
    training_keys.to_csv(filename_keys,index=False,header=['w','s','a','d'])


def move(y):
    maxi=0
    y=y.flatten()
    for i in range(0,len(y)):
        if(y[i]>y[maxi]):maxi=i
        print(round(y[i],2),end=',')
    arr=['w','s','a','d']#no key is not required
    print(arr[maxi])
    if arr[maxi]=='w' : accelerate()
    elif arr[maxi]=='s':  deaccelerate()
    elif arr[maxi]=='a':   left()
    elif arr[maxi]=='d':  right()
    
    
def drive(pos):
    model=load_model('model/model.h5')
    for i in range(1,4):
        print(i ,'')
        time.sleep(1)
    print('driving now...(press esc to stop)')
    while True:
        intsarray,height,width=get_screen(pos,win32gui, win32ui, win32con, win32api)
        img=process_img(intsarray,height,width,np,cv2)
        img=img.flatten()
        img=np.array(img)/255 
        img.shape=(1,30,30,3)
        y=model.predict(img)
        move(y);
        img.shape=(30,30,3)
        cv2.imshow('Driving',img)
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break;


def main():
  

    pos=get_position(pag)
    if pos==None:
        f=open('data/frames-pos.temp','r')
        pos=eval(f.read())
        f.close()
    else:
        f=open('data/frames-pos.temp','w')
        f.write(str(pos))
        f.close()
    
    print('Frames will be captured at : ',pos)
    inp=int(input('You want to Train(0) or Test(1)? Press 0 or 1.'))
    if(inp==0):
        train(pos)
    if(inp==1):
        drive(pos)
  
if __name__== "__main__":
  main()





