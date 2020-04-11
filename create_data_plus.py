from PIL import Image
import os,glob
import numpy as np
from sklearn import model_selection

classes = ["monkey", "cat", "dog"]
num_classes = len(classes)
image_size = 50, 50
num_testdata = 100

#read images
X_train = []
X_test = []
Y_train = []
Y_test = []

for index, classlabel in enumerate(classes):
    photo_dir = "../images/" + classlabel
    files = glob.glob(photo_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 170:
            break
        else:
            im = Image.open(file)
            im = im.convert('RGB')
            im = im.resize(image_size)
            data = np.asarray(im)

            if i < num_testdata:
                X_test.append(data)
                Y_test.append(index)
            else:
                X_train.append(data)
                Y_train.append(index)

                for angle in range(-20,20,5):
                    img_r = im.rotate(angle)
                    data = np.asarray(img_r)
                    X_train.append(data)
                    Y_train.append(index)

                    img_rev = im.transpose(Image.FLIP_LEFT_RIGHT)
                    data = np.asarray(img_rev)
                    X_train.append(data)
                    Y_train.append(index)

X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

#X = np.array(X)
#Y = np.array(Y)

#X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test)
np.save("./animal_plus.npy", xy)
