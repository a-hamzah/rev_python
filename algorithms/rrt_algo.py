import numpy as np
import matplotlib.pyplot as plt
import random

# Settings of python plots
from matplotlib.pyplot import rcParams
np.set_printoptions(precision=3, suppress=True)
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']
plt.rcParams['font.size'] = 22

# TreeNode Class
class treeNode():
    def __init__(self, locationX, locationY):
        self.locationX = locationX
        self.locationY = locationY
        self.children = []
        self.parent = None