from calculator import EnergyCalculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_dual_gradient(self):
        self.test_data = [
            [(0,   0,   0), (255, 153, 153), (0,   0,   0)],
            [(255, 204,  51), (255, 204, 153), (255, 205, 255)],
            [(0,   0,   0), (255, 255, 153), (0,   0,   0)]
        ]
        calc = EnergyCalculator(self.test_data, "dg")
        result = calc.get_energy()
        print("test data for dual_gradient:")
        print(self.test_data)
        print("\nresult:")
        print(result)
        self.assertEqual(result[1][1],52204**0.5)

if __name__ == "__main__":
    unittest.main()