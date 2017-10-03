# **AutonomousCarAI**
## Description

Training a car to drive autonomously. A deep learning implementation of simple self driving car.  The aim of the project is to train a car to drive in a game terrain by capturing the frames and the keys. Each frame has been converted to a *1x2700* numpy array corresponds to which there are keys *w,s,a,d*.

## Prerequisites

The python library used to capture frames is ***win32api*** which is only available on Windows. Because of this, it can't run on Linux. As an alteranative, ***pyscreenshot*** can be used in Linux but it is extremely slow to capture frames ~ 10fps. ***Keras*** with tensorflow backend has been used to train the model. 



## How it works

 - Run the ***game.exe***. Once the red screen with the note "Press Space" appears, run ***main.py***. Let main.py know the location of the game. Do not press space unless it finds the game screen.
 - ***main.py*** will capture the location of the game and will ask whether to train, test, or quit. 
 - Choose an option:
**Training** use *w*, *a*, *s*, *d* to move the car on the road, and press *q* to stop training. This will collect data and store to */data/* folder. Once data has been collected, run ***model.py*** to create a trained model for the self driving car  in the */model/* folder. Now this model can be used for testing.
**Testing** Testing here refers to driving. Once there is a trained model, this option can be used. Just select the option and let the car drive itself. To stop testing, put the cursor on the opencv screen windows and press *esc*.




## Game Link

The link of the car game to be trained: 
https://www.dropbox.com/s/ul3s4i0trnohsih/game.zip?dl=0


