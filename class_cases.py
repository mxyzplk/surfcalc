import os
import numpy as np

class cases():
    def __init__(self):
        self.labels = {
            "Mach": 0,
            "EAS": 1,
            "AOA": 2,
            "Beta": 3,
            "p": 4,
            "q": 5,
            "r": 6,
            "pp": 7,
            "qp": 8,
            "rp": 9,
            "Nx": 10,
            "Ny": 11,
            "Nz": 12,
            "xCG": 13,
            "yCG": 14,
            "zCG": 15,
            "Def": 16,
            "Conf": 17
        }
        #
        f = open("cases.txt", "r")
        #
        self.ids = []
        #
        f.readline()
        #
        Lines = f.readlines()
        self.ncases = len(Lines)
        self.flight_data = np.empty((17,self.ncases),dtype="float")
        #
        i = 0
        for line in Lines:
            temp = line.strip("\n").split()
            self.ids.append(temp[0])
            for j in range(17):
                self.flight_data[j,i] = float(temp[j+1])
            i = i + 1
        #
        f.close()
        #


