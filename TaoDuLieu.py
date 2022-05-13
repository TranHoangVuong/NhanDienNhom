import cv2
import glob
import numpy as np
import pickle

X_train = []
Y_train = []

for filename in glob.glob("./img/Vuong/*.jpg"):
    img = cv2.resize(cv2.imread(filename),(150,150))
    X_train.append(img)
    Y_train.append(2)

X_train = np.array(X_train)
Y_train = np.array(Y_train)
print(X_train.shape)
print(Y_train.shape)
with open("data(1nguoi).pickle","wb") as f:
    pickle.dump((X_train, Y_train),f)