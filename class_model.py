import numpy as np
import os
import math_functions

class grid_model():
    def __init__(self, n_grids, n_elements, e_type):
        #
        self.grids = np.empty((n_grids,3), dtype=float)
        self.centroid = np.empty((n_elements,3), dtype=float)
        #
        if (e_type == 3):
            self.model = np.empty((n_elements,3), dtype=int)
        elif (e_type == 4):
            self.model = np.empty((n_elements,4), dtype=int)
        #
        self.read_grids(n_grids)
        self.read_elements(e_type, n_elements)
        #
        self.define_centroid(n_elements, e_type)


    def read_grids(self, n_grids):
        #
        # Coordinates in global C/S
        #
        f = open("grids.txt", "r")
        #
        for i in range(n_grids):
            line = f.readline()
            self.grids[i,0:2] = float(line.split())
        #
        f.close()
     

    def read_elements(self, e_type, n_elements):
        #
        f = open("elements.txt", "r")
        #
        for i in range(n_elements):
            line = f.readline()
            if (e_type == 3):
                self.model[i,0:2] = float(line.split())
            elif (e_type == 4):
                self.model[i,0:3] = float(line.split())
        #
        f.close()
        

    def define_centroid(self, n_elements, e_type):
        for i in range(n_elements):
            for j in range(e_type):
                self.centroid[i,0] = self.centroid[i,0] + self.grids[self.model[i,j],0]
                self.centroid[i,1] = self.centroid[i,1] + self.grids[self.model[i,j],1] 
                self.centroid[i,2] = self.centroid[i,2] + self.grids[self.model[i,j],2]
            #
            self.centroid[i,0] = self.centroid[i,0] / float(e_type)
            self.centroid[i,1] = self.centroid[i,1] / float(e_type)
            self.centroid[i,2] = self.centroid[i,2] / float(e_type)


class cp_model():
    def __init__(self, n_elements, n_par, n_dists):
        #
        self.cps = np.empty((n_elements,n_dists), dtype=float)
        self.par = np.empty((n_dists, n_par), dtype=float)
        #
        self.read_cps(n_dists, n_par, n_elements)


    def read_cps(self, n_dists, n_par, n_elements):
        f = open("cps.txt", "r")
        #
        self.par[:,i] = f.readline().split()
        #
        self.cps[i,:] = f.readline().split()
        #         
        f.close()
