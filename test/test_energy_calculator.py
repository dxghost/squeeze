from energy_calculators.calculator import EnergyCalculator
import unittest
import math

class TestCalculator(unittest.TestCase):

    def test_dual_gradient(self):
        self.test_data = [
            [(0,   0,   0), (255, 153, 153), (0,   0,   0)],
            [(255, 203,  51), (255, 204, 153), (255, 205, 255)],
            [(0,   0,   0), (255, 255, 153), (0,   0,   0)]
        ]
        calc = EnergyCalculator(self.test_data, "dg")
        result = calc.get_energy()
        self.assertEqual(result[1][1],math.sqrt(52024))

if __name__ == "__main__":
    unittest.main()