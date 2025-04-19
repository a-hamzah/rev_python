from spatialmath.base import *
import numpy as np
from math import atan2, cos, sin


class Pose3D(np.ndarray):

    def __new__(cls, input_array):  # first method

        assert input_array.shape == (3, 1), "mean must be a 3x1 vector"

        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # Finally, we must return the newly created object:
        return obj

    def oplus(AxB, BxC):  # method that will compound two poses (Second Method)

        # TODO: to be completed by the student (DONE``)

        # AxB (3x1)
        AxC = np.array([[AxB[0, 0] + BxC[0, 0] * cos(AxB[2, 0]) - BxC[1, 0]*sin(AxB[2, 0])],

                        [AxB[1, 0] + BxC[0, 0] *
                            sin(AxB[2, 0]) + BxC[1, 0]*cos(AxB[2, 0])],


                        [AxB[2, 0] + BxC[2, 0]]
                        ])
        return Pose3D(AxC)

        pass

    def ominus(AxB):
        # TODO: to be completed by the student (DONE)
        BxA = np.array([[-AxB[0, 0]*cos(AxB[2, 0]) - AxB[1, 0]*sin(AxB[2, 0])],
                        [AxB[0, 0]*sin(AxB[2, 0]) - AxB[1, 0]*cos(AxB[2, 0])],
                        [-AxB[2, 0]]
                        ])
        return Pose3D(BxA)

        pass


AxB = np.array([[1],
                [2],
                [np.pi/2]])
# print(AxB)
BxC = np.array([[3],
                [4],
                [np.pi]])
# print(BxC)

AxC = Pose3D(AxB).oplus(BxC)
# print(AxC)

print("AxC=", AxC.T)


CxA = Pose3D(AxC).ominus()

print("CxA=", CxA.T)
