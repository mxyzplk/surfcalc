import numpy as np
import scipy.interpolate.ndgriddata

class Aero:
    def __int__(self, ngrids, nalphas, nbetas):
        if nbetas == 0:
            self.cps = np.empty(ngrids,nalphas)
        elif nalphas == 0:
            self.cps = np.empty(ngrids, nbetas)
        else:
            self.cps = np.empty(ngrids, nalphas, nbetas)

    def interp_grid_1d(self, grid, angle):
        pass


    def interp_grid_2d(self, grid, alpha, beta):
        pass
