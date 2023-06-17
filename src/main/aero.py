import numpy as np
import scipy.interpolate.ndgriddata


class Set:
    def __int__(self, ndefs):
        self.ndefs = ndefs
        self.nmachs = np.empty(ndefs)
        self.machs = None
        self.defs = None
    def set_distributions(self):
        pass
class Aero:
    def __int__(self):
        self.alpha = None
        self.beta = None
        self.nalphas = None
        self.nbetas = None
        self.cps = None

    def set_variables(self, ngrids, nalphas, nbetas):
        self.alpha = np.empty(int(nalphas))
        self.beta = np.empty(int(nbetas))
        self.nalphas = int(nalphas)
        self.nbetas = int(nbetas)

        if int(nbetas) == 0:
            self.cps = np.empty([int(ngrids), int(nalphas)])
        elif int(nalphas) == 0:
            self.cps = np.empty([int(ngrids), int(nbetas)])
        else:
            self.cps = np.empty([int(ngrids), int(nalphas), int(nbetas)])

    def interp_grid_1d(self, grid, angle):
        pass

    def interp_grid_2d(self, grid, alpha, beta):
        pass

    def set_coefficients_1d(self, coef, grid, angle):
        self.cps[grid, angle] = coef

    def set_coefficients_2d(self, coef, grid, alpha, beta):
        self.cps[grid, alpha, beta] = coef

    def set_alphas(self, angles):
        for i in range(self.nalphas):
            self.alpha[i] = angles[i]

    def set_betas(self, angles):
        for i in range(self.nbetas):
            self.beta[i] = angles[i]
