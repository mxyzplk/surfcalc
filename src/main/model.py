import numpy as np
import os
import sys
from aero import Set
from cs import CS


class Model:
    def __int__(self):
        self.n_grids = None
        self.n_elements = None
        self.grids = None
        self.connects = None
        self.cps = None
        self.elements = None
        self.mesh = None
        self.coefs = []
        self.control = np.empty(3)  # mass | deflection | local cs

    def read_config(self):
        abs_path = sys.path[0]
        base_name = os.path.dirname(abs_path)
        options_path = os.path.join(base_name, "src/resources/config.txt")
        with open(options_path, "r") as file:
            line = file.readline().split()
            # mass config
            self.control[0] = int(line[0])
            # number of deflections
            line = file.readline().split()
            self.control[1] = int(line[0])
        file.close()

    def load_grids_txt(self, file_path):

        with open(file_path, "r") as file:
            # reading first line containing number of grids
            line = file.readline().strip()
            self.n_grids = int(line)
            # defining grids array
            self.grids = np.empty(self.n_grids, 3)
            # reading grids
            i = 0
            while i < self.n_grids:
                line = file.readline().strip()
                self.grids[i, :] = line.split()
                i += 1
        # closing grids file
        file.close()

    def load_connectivity_txt(self, file_path):

        with open(file_path, "r") as file:
            # reading first line containing number of elements
            line = file.readline().strip()
            self.n_elements, self.mesh = map(int, line.split())
            # defining connectivity array
            self.connects = np.empty(self.n_grids, self.mesh)
            # reading connectivity
            i = 0
            while i < self.n_elements:
                line = file.readline().strip()
                self.connects[i, :] = line.split()
                i += 1
        # closing connectivity file
        file.close()

    def define_elements(self):
        # define elements array containing center coordinates(x, y, z), total area, axy, axz, ayz
        self.elements = np.empty([self.n_elements, 7])

        # panel vertices
        vertices = np.empty([self.mesh, 3])

        i = 0
        while i < self.n_elements:
            j = 0
            while j < self.mesh:
                k = 0
                while k < 3:
                    vertices[j, k] = self.grids[self.connects[i, j], k]
                    k += 1
                j += 1
            k = 0
            while k < 3:
                # defining element center
                self.elements[i, k] = sum(vertices[:, k]) / self.mesh

            self.elements[i, 3:6] = Model.calculate_panel_area(vertices)
            i += 1

    @staticmethod
    def calculate_panel_area(vertices):
        num_edges = len(vertices)

        if num_edges == 3:
            return Model.calculate_tri_area(vertices)
        elif num_edges == 4:
            return Model.calculate_quad_area(vertices)
        else:
            raise ValueError("Invalid number of panel edges. Only 3 or 4 edges supported.")

    @staticmethod
    def calculate_tri_area(vertices):
        # Calculate the cross product of two edges
        vector1 = vertices[1] - vertices[0]
        vector2 = vertices[2] - vertices[0]
        return 0.5 * np.cross(vector1, vector2)

    @staticmethod
    def calculate_quad_area(vertices):
        vector1 = vertices[2] - vertices[0]
        vector2 = vertices[3] - vertices[1]
        return 0.5 * np.cross(vector1, vector2)

    def load_coefs(self, file_path):
        pass