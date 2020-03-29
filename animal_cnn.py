from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras,utils import np_utils
import numpy as np

classes = ["monkey", "cat", "dog"]
num_classes = len(classes)
image_size = 50, 50

def main():
    X_train, X_test, Y_train, Y_test = np.load("./animal.npy")
    X_train = X_train.astype("float") / 256
    X_test = X_test.astype("float") / 256
    Y_train = np_utils.to_categorical(Y_train, num_classes)
    Y_test = np_utils.to_categorical(Y_test, num_classes)

    model = model_train(X_train, Y_train)
    model_eval(model, X_test, Y_test)

def model_train():
    model = Sequential()
    model.add(Conv2D(32,(3,3), padding='same', input_shape=X_train[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64,(3,3), padding='same'))
    model.add(Conv2D(64,(3,3)))
    model.add(MaxPooling2D(pool_size(2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3))
    model.add(Activation('softmax'))

    opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

    model.compile(loss='categolical_crossentropy',
                    oprimizer=opt, metrics=['accuracy'])
