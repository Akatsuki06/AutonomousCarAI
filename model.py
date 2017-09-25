
import pandas as pd
import numpy as np
import glob

import keras
from keras.models import load_model,Sequential
from keras.layers import Dense, Flatten,Conv2D, MaxPooling2D,Convolution2D,Dropout


frames=pd.DataFrame()
keys=pd.DataFrame()
nooffiles=len(glob.glob("data/*frames*.csv"))
df_frames = (pd.read_csv(f) for f in glob.glob("data/*frames*.csv"))
frames  = pd.concat(df_frames, ignore_index=True)
df_keys = (pd.read_csv(f) for f in glob.glob("data/*keys*.csv"))
keys = pd.concat(df_keys, ignore_index=True)
X=np.array(frames)
y=np.array(keys)

print('no of files being trained : ' , nooffiles);
frames.head()
frames.shape

keys.head()


X=np.array(frames)/255 
X.shape=(X.shape[0],30,30,3)


print(X.shape,y.shape) 


input_shape=(30, 30,3)
batch_size = 128
num_classes = 4
epochs = 20
model = Sequential()
model = Sequential()
 
model.add(Convolution2D(32, kernel_size=(5, 5), activation='relu',
                        input_shape=input_shape))
model.add(Convolution2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
 
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))


model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])

model.fit(X, y,batch_size=batch_size,epochs=epochs,verbose=1)

#           validation_data=(x_test, y_test),
#           callbacks=[history]
# score = model.evaluate(x_test, y_test, verbose=0)
modelname= 'model/'+str(len(glob.glob("model/*")))
model.save(modelname)



