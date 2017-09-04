
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
frames=pd.read_csv('data1/training_frames.csv')
keys=pd.read_csv('data1/training_keys.csv')
frames=frames.append(pd.read_csv('data2/training_frames.csv'))
keys=keys.append(pd.read_csv('data2/training_keys.csv'))
X=np.array(frames)
y=np.array(keys)


# In[2]:


frames.head()
frames.shape


# In[3]:


keys.head()


# In[4]:



print(X.shape[1])
# X/=255
print(X.shape)
X=X.reshape((X.shape[0],30,30,1))


# In[5]:


print(X.shape,y.shape) #much better!!


# In[6]:


X=X.astype('float')
X/=255


# In[7]:


import keras
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D,Convolution2D,Dropout
from keras.models import Sequential


# In[8]:


input_shape=(30, 30,1)
batch_size = 128
num_classes = 5
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
model.add(Dense(5, activation='softmax'))


# In[9]:


model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])

model.fit(X, y,batch_size=batch_size,epochs=epochs,verbose=1)

#           validation_data=(x_test, y_test),
#           callbacks=[history]
# score = model.evaluate(x_test, y_test, verbose=0)


# In[13]:


from keras.models import load_model
model.save('model1.h5')


# In[ ]:





# In[ ]:






