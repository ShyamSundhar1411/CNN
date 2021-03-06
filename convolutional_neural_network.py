#Convolution Neural Network
#Required Libraries
import tensorflow as t
import pandas as d
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import image

#Data Preprocessing
#Training Set
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
training_set= train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
#Test Set
test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
#Convolusion
cnn=t.keras.models.Sequential()
cnn.add(t.keras.layers.Conv2D(filters=32,kernel_size=3,activation = 'relu',input_shape=[64,64,3]))
#Pooling
cnn.add(t.keras.layers.MaxPool2D(pool_size=2,strides=2))
#Adding Second Convolution Layer
cnn.add(t.keras.layers.Conv2D(filters=32,kernel_size=3,activation = 'relu'))
cnn.add(t.keras.layers.MaxPool2D(pool_size=2,strides=2))
#Flattening
cnn.add(t.keras.layers.Flatten())
#Full Connection
cnn.add(t.keras.layers.Dense(units = 128,activation = 'relu'))
#Output Layer
cnn.add(t.keras.layers.Dense(units = 1,activation = 'sigmoid'))
#Training
#cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
#cnn.fit(x = training_set, validation_data = test_set, epochs = 25)
#Predicting output
p = image.load_img('dataset/single_prediction/untitled.jpg',target_size=(64,64))
p = image.img_to_array(p)
p = np.expand_dims(p ,axis = 0 )
result = cnn.predict(p)
training_set.class_indices
if result[0][0] == 1:
    print('dog')
elif result[0][0] == 0:
    print('cat')
else:
    print('bird')
