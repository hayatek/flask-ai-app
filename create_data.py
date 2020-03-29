from PIL import Image
import os,glob
import numpy as np
from sklearn import model_selection

classes = ["monkey", "cat", "dog"]
num_classes = len(classes)
image_size = 50, 50

#read images
X = []
Y = []
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
            X.append(data)
            Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test)
np.save("./animal.npy", xy)
