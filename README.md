# **AutonomousCarAI**
## Description

Training a car to drive autonomously. A deep learning implementation of a simple self-driving car. The aim of the project is to train a car to drive in a game terrain by capturing the frames and the keys. Each frame is converted to a *1x2700* numpy array to which there are corresponding keys: *w,s,a,d*.

## Prerequisites

The python library used to capture frames is ***win32api*** which is only available on windows. As an alteranative ***pyscreenshot*** can be used in linux but it is captures frames extremely slow (~ 10fps). ***Keras*** with tensorflow backend has been used to train the model. 


## How does it works?

 1. Run ***game.exe***.
 2. Once the red screen with the note "Press Space" appears run ***main.py***. Let main.py know the location of the game. So don't press space until it finds the game screen.
 3. ***main.py*** will capture the location of the game and will ask whether to train, test or quit. 
 4. Choose an option:
    - **Training**: use *w*, *a*, *s*, *d* to move the car on the road and press *q* to stop training. This will collect data and store it to `data/` folder. Once data has been collected, run ***model.py*** to create a trained model for the self-driving car in the `model/` folder. Now this model can be used for testing.
    - **Testing**: Testing here refers to driving. Once there is a trained model this option can be used. Just select the option and let the car drive itself. To stop testing, put the cursor on the opencv screen window and press *esc*.


## Game Link

The link of the car game to be trained:
https://www.dropbox.com/s/ji1ywiaj7s1kin7/Game-Updated.rar?dl=0
