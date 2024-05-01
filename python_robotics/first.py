import roboticstoolbox as rtb
from spatialmath.base import *
import numpy as np

# angle = np.deg2rad(30)
# rot_mat = rotz(angle)
# -------------------------
# AxB = np.array([1, 2, np.pi])
# print(AxB[1])
# BxC = np.array([3, 4, np.pi])
# print(BxC)

# T = transl(0.5, 0.0, 0.0)
# print(T)
# -------------------------
# rot_mat1 = rotz(90)

# T = transl(0.5, 0.0, 0.0) @ rpy2tr(0.1, 0.2,0.3, order='xyz') @ trotz(30, 'deg')
# print(T)

# print(rot_mat)
# print(rot_mat1)
AxB = np.array([[1],
                [2],
                [np.pi]])

# poseVec_B = np.array([0, 2, 0])
print(AxB[0, 0])
# print(poseVec_A[1])  ------ works but don't use
# print(poseVec_A.shape)
# res = rot_mat * poseVec_B
# print(res)
# # rotMatrix = rtb.rot
# his_array = np.array([1, 2, 3])

# my_array = np.ndarray((3, 1))

# vector_column = np.array([[1],
#                           [2],
#                           [3]])
# print(my_array)
# print(his_array)
# print(vector_column)
# print(poseVec_A)
