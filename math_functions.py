import numpy as np
from scipy.interpolate import griddata

def area_element(nodes):
    # Nodes is a numpy array with 3 or 4 elements, 
    # each holding the information of a x,y,z coordinates.
    # Area calculation is performed considering the order the nodes
    # are stored in the vector obeying the right hand rule.
    # Function return the Area vectors and the resultant area
    # in a 4 elements numpy vector (Axy, Ayz, Axz, Atot).
    #        
    # Nodes [(x1, y1, z1),
    #       (x2, y2, z2)
    #       (x3, y3, z3)
    #       (x4, y4, z4)] (Optional)
    #
    # Check the number of elements.
    #
    area = np.empty(4, dtype=float)
    u = np.empty(3, dtype=float)
    v = np.empty(3, dtype=float)
    normal = np.empty(3, dtype=float)
    versor = np.empty(3, dtype=float)
    #
    num_elements, num_dim = nodes.shape
    #
    if num_elements == 3:
        u = pts2vec(nodes[0,0:2],nodes[1,0:2])
        v = pts2vec(nodes[1,0:2],nodes[2,0:2])
        normal = cross_product(u,v)
        versor = vers_vector(normal)
        area[3] = 0.5*mod_vector(normal)
        area[0] = versor[0] * area[3]   #Ayz
        area[1] = versor[1] * area[3]   #Axz
        area[2] = versor[2] * area[3]   #Axy
        return area
    elif num_elements == 4:
        u = pts2vec(nodes[0,0:2],nodes[2,0:2])
        v = pts2vec(nodes[1,0:2],nodes[3,0:2])
        normal = cross_product(u,v)
        versor = vers_vector(normal)
        area[3] = 0.5*mod_vector(normal)
        area[0] = versor[0] * area[3]   #Ayz
        area[1] = versor[1] * area[3]   #Axz
        area[2] = versor[2] * area[3]   #Axy
        return area
    #
    return area


def cross_product(u, v):
    # Cross product function between two vectors u^v
    # Vectors are numpy arrays with 3 elements (x, y, z)
    # Results is given in the form of a vector in the same form
    result = np.empty(3,dtype=float)
    #
    result[0] = u[1] * v[2] - u[2] * v[1]
    result[1] = -1 * (u[1] * v[2] - u[2] * v[1])
    result[2] = u[1] * v[2] - u[2] * v[1]
    #
    return result


def vers_vector(u):
    # normalize a vector
    result = np.empty(3,dtype=float)
    #
    mod = mod_vector(u)
    #
    result[0] = u[0] / mod
    result[1] = u[1] / mod
    result[2] = u[2] / mod
    #
    return result


def mod_vector(u):
    # Module of a vector
    result = (u[0]^2 + u[1]^2 + u[2]^2)^0.5
    return result


def pts2vec(x,y):
    # Vector v = y-x
    result = np.empty(3,dtype=float)
    #
    result[0] = y[0] - x[0]
    result[1] = y[1] - x[1]
    result[2] = y[2] - x[2]
    #
    return result


def interp_cps(par_tgt, par, cps):
    #
    cp = griddata(par, cps, par_tgt, method='linear')
    #
    return cp


def local_aoa(Ux, p, radius):
    #
    aoa = radius * p / Ux
    #
    return aoa

