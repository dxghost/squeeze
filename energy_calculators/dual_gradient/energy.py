from energy_calculators.factory import EnergyFactory
import numpy as np
import math


class DualGradient(EnergyFactory):
    name = "dg"
    def __init__(self):
        pass

    def compute(self, rgb_matrix):
        x_len = len(rgb_matrix[0])
        y_len = len(rgb_matrix)
        energy = np.zeros((y_len, x_len))
        for i in range(1, y_len-1):
            for j in range(1, x_len-1):
                r2x = int(rgb_matrix[i][j+1][0]) - int(rgb_matrix[i][j-1][0])
                b2x = int(rgb_matrix[i][j+1][1]) - int(rgb_matrix[i][j-1][1])
                g2x = int(rgb_matrix[i][j+1][2]) - int(rgb_matrix[i][j-1][2])
                deltax = math.pow(r2x, 2) + math.pow(b2x, 2) + math.pow(g2x, 2)

                r2y = int(rgb_matrix[i+1][j][0]) - int(rgb_matrix[i-1][j][0])
                b2y = int(rgb_matrix[i+1][j][1]) - int(rgb_matrix[i-1][j][1])
                g2y = int(rgb_matrix[i+1][j][2]) - int(rgb_matrix[i-1][j][2])
                deltay = math.pow(r2y, 2) + math.pow(b2y, 2) + math.pow(g2y, 2)

                energy[i][j] = math.sqrt(int(deltax+deltay))

        return energy
