import numpy as np
from energy_calculators.dual_gradient.energy import DualGradient


class EnergyCalculator:
    def __init__(self,rgb_matrix,method):
        self.rgb_matrix = rgb_matrix
        self.method = method
        self.energy = []
    
    def get_energy(self):
        if self.method == "dg":
            engine = DualGradient()
            self.energy = engine.compute(self.rgb_matrix)
            return self.energy

        raise ValueError("method not found")
