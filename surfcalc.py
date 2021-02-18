import os
import numpy as np
import class_option
import class_cases
import class_model

#
# Software that calculates the aerodynamic and inertial forces on a surface.
#
# Input cases data (order must be respected in cases.txt)     Code
#
# Mach Number                                                 Mach
# EAS (Equivalent Airspeed - m/s)                             EAS
# Angle of Attack (deg)                                       AOA
# Sideslip Angle (deg)                                        Beta
# p (Roll) (rad/s)                                            p
# q (Pitch) (rad/s)                                           q
# r (Yaw) (rad/s)                                             r
# pp (Roll Acc) (rad/s2)                                      pp
# qp (Pitch Acc) (rad/s2)                                     qp
# rp (Yaw Acc) (rad/s2)                                       rp
# Nx (Load Factor at CG - X Axis)                             Nx
# Ny (Load Factor at CG - Y Axis)                             Ny
# Nz (Load Factor at CG - Z Axis)                             Nz
# X C.G. (Center of Gravity - X Coordinate)                   xCG
# Y C.G. (Center of Gravity - X Coordinate)                   yCG
# Z C.G. (Center of Gravity - X Coordinate)                   zCG
# Surface Deflection (deg)                                    Def
# Surface Configuration (Integer)                             Conf
#
# Orientations
# 
# p (+) : left wing up
# q (+) : nose up
# r (+) : nose left
#
# Nx (+) : stream
# Ny (+) : right
# Nz (+) : downward
#
#

analise = class_cases.cases()
