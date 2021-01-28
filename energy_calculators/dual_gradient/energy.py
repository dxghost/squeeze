from factory import EnergyFactory


class DualGradient(EnergyFactory):
    def __init__(self):
        pass

    def compute(self, rgb_matrix):
        return [
            [0, 0         , 0],
            [0, 52204**0.5, 0],
            [0, 0         , 0]
        ]
