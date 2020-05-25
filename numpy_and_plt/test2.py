# ===========================
# import library
# ===========================
import tensorflow as tf
from tensorflow import keras
from keras import models
from keras.models import Sequential
from keras import layers
from keras.datasets import mnist
from keras.utils import to_categorical

from keras.layers import Dense
from keras.layers import BatchNormalization
from keras.layers import Activation
from keras.layers import Dropout
import matplotlib.pyplot as plt
#===========================
# import mnist dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data(path="mnist.npz")
#===========================
# reshape input data
train_images	= train_images.reshape((60000,28,28,1))
train_images 	= train_images.astype('float32')/255
test_images 	= test_images.reshape((10000,28,28,1))
test_images 	= test_images.astype('float32')/255
#===========================
# train labels
#===========================
train_labels = to_categorical(train_labels) #one-hot encoding
test_labels = to_categorical(test_labels)   #one-hot encoding

#===========================
# model creation by sequential class
#===========================
model = models.Sequential()
model.add(layers.Conv2D(32,(3,3,),activation='relu', input_shape=(28,28,1),padding='same'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64,(3,3,),activation='relu'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64,(3,3,),activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(10,activation='softmax'))
print(model.summary())
#===========================
# Tensorboard usage
#===========================
tensorboard = keras.callbacks.TensorBoard(log_dir="E:\\tensorflow\log")
#===========================
# model compile and training
#===========================
model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images,train_labels,epochs=1, batch_size=65)

from keras.models import load_model
from keras.models import save_model
models.save_model(model, 'mnist_model.h5');  #저장(구성정보,가중치,손실함수,학습상태)
model = load_model('mnist_model.h5')

loss, acc = model.evaluate(test_images,test_labels)
print('acc : ', acc); print('loss : ', loss);
plt.plot(acc)
