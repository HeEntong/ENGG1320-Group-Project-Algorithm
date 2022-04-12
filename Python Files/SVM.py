from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *

def shootingType(dataType):
    dataDict = {
        "upperlimb_left":0, "upperlimb_right":1, "thigh_left":2,
        "thigh_right":3, "averAngularVelocity":4, 
        
    }
    
x = [[0,0],[3,3],[2,5]]
y = [0,1,0]
clf = svm.SVC()
clf.fit(x, y)
print(clf.predict([[23,1]]))
print(clf.support_vectors_)