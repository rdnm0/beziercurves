# beziercurves
matplotlib Path forked from torresjrjr

Path fork // animations tweaked / added

HOW TO USE - 
pip install matplotlib numpy
to run in intwindow - pip install ipykernel

from Bezier import Bezier
import numpy as np

2D example -
t_points = np.arange(0, 1, 0.01) #................................. 
points1 = np.array([[0, 0], [0, 8], [5, 10], [9, 7], [4, 3]]) #....
You can plot your creations with matplotlib.

import matplotlib.pyplot as plt

plt.figure()
plt.plot(
	curve1[:, 0],   
	curve1[:, 1]    
)
plt.plot(
	points1[:, 0],  
	points1[:, 1],   
)
plt.grid()
plt.show()

The resulting plot
