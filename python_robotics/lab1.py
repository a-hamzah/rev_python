from spatialmath import *
import numpy as np
from math import *

class Pose3D(np.ndarray):
    def __new__(cls, my_array):
        # checking the input array (3,1) and printing the message in "" if assertion fails
        assert my_array.shape == (3, 1), "Mean must be a 3x1 vector"
        
