from PIL import Image
from numpy import asarray
from energy_calculators.calculator import EnergyCalculator

# load the image
image = Image.open('test_data/input.jpg')
# np array rgb
data = asarray(image)
calculator = EnergyCalculator(data,"dg")
energy = calculator.get_energy()

# show image
image2 = Image.fromarray(data)
image2.show()


image2 = Image.fromarray(energy)
image2.show()