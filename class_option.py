import os
import numpy as np

class options():
    def __init__(self):
        #
        f = open("options.txt", "r")
        #
        self.npars = int(f.readline().split())
        #
        self.pars = f.readline().split()
        #
        self.localcsopt = int(f.readline().split())
        #
        if (self.localcsopt == 1):
            #
            self.localcs = np.empty((4,3), dtype=float)
            for i in range(4):
                self.localcs[i,0:3] = float(f.readline().split())
            #
        elif (self.localcsopt == 0):
            pass
        #
        self.rloadsopt = int(f.readline().split())
        #
        if (self.rloadsopt == 1):
            #
            self.integration_line_npt = int(f.readline().split())
            self.integration_line = np.empty((self.integration_line_npt,3), dtype=float)
            #
            for i in range(self.integration_line_npt):
                self.integration_line[i,0:3] = float(f.readline().split())
            #
        elif (self.rloadsopt == 0):
            pass
        #
        self.massmodelopt = int(f.readline().split())
        self.envopt = int(f.readline().split())
        self.n_grids, self.n_elements, self.n_dists = int(f.readline().split())
        #
        f.close()
        #



