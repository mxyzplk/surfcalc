import numpy as np


class CS:
    def __int__(self, n):
        self.points = np.empty(int(n), 4, 3)
        self.unit_vector = np.empty(int(n), 3, 3)
        self.envelope = np.empty(int(n), 6)

    def load_cs(self, filepath):
        pass

