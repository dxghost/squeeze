import numpy as np
from energy_calculators.dual_gradient.energy import DualGradient

# Register your calculator here
CALCULATORS = [
    DualGradient,
]

class EnergyCalculator:
    def __init__(self,rgb_matrix,method):
        self.rgb_matrix = rgb_matrix
        self.method = method
        self.energy = []
    
    def get_energy(self):
        for method in CALCULATORS:
            if self.method == method.name:
                engine = method()
                self.energy = engine.compute(self.rgb_matrix)
                return self.energy

        raise ValueError("method not found")
