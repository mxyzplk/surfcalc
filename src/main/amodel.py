import numpy as np


class Amodel:
    def __int__(self):
        self.n_grids = None
        self.n_elements = None
        self.grids = None
        self.connects = None
        self.cps = None
        self.elements = None
        self.mesh = None

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
        self.elements = np.empty(self.n_elements, 7)

        # panel vertices
        vertices = np.empty(self.mesh, 3)

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

            self.elements[i, 3:6] = self.calculate_panel_area(vertices)
            i += 1

    def calculate_panel_area(vertices):
        num_edges = len(vertices)

        if num_edges == 3:
            return calculate_triangle_area(vertices)
        elif num_edges == 4:
            return calculate_polygon_area(vertices)
        else:
            raise ValueError("Invalid number of edges. Only 3 or 4 edges supported.")

    def calculate_triangle_area(vertices):
        # Calculate the cross product of two edges
        edge1 = vertices[1] - vertices[0]
        edge2 = vertices[2] - vertices[0]
        cross_product = np.cross(edge1, edge2)

        # Calculate the magnitude of the cross product
        area = 0.5 * np.linalg.norm(cross_product)

        return area

    def calculate_polygon_area(vertices):
        # Divide the polygon into triangles and sum their areas
        total_area = 0.0
        num_vertices = len(vertices)

        for i in range(num_vertices - 2):
            triangle_vertices = np.array([vertices[0], vertices[i + 1], vertices[i + 2]])
            triangle_area = calculate_triangle_area(triangle_vertices)
            total_area += triangle_area

        return total_area

    def load_coefficients(self, filename):
        pass
