from energy_calculators.calculator import EnergyCalculator
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

class SeamCarve:
    def __init__(self, image_array):
        self.image = image_array
        self.width = len(image_array[0])
        self.height = len(image_array)
        
        calculator = EnergyCalculator(self.image, "dg")
        self.energy = calculator.get_energy()

    def update(self, image_array):
        self.image = image_array
        self.width = len(image_array[0])
        self.height = len(image_array)

        calculator = EnergyCalculator(self.image, "dg")
        self.energy = calculator.get_energy()

    def rotate(self, k):
        self.image = np.rot90(self.image, k)
        self.energy = np.rot90(self.energy, k)
        self.width = len(self.image[0])
        self.height = len(self.image)

    def get_minimum_seam(self):
        # Adapted from https://github.com/andrewdcampbell/seam-carving/blob/master/seam_carving.py
        # and andrew adapted it from https://karthikkaranth.me/blog/implementing-seam-carving-with-python/
        energy = self.energy
        backtrack = np.zeros_like(energy, dtype=np.int)

        for i in range(1, self.height):
            for j in range(0, self.width):
                if j == 0:
                    idx = np.argmin(energy[i - 1, j:j + 2])
                    backtrack[i, j] = idx + j
                    min_energy = energy[i-1, idx + j]
                else:
                    idx = np.argmin(energy[i - 1, j - 1:j + 2])
                    backtrack[i, j] = idx + j - 1
                    min_energy = energy[i - 1, idx + j - 1]

                energy[i, j] += min_energy

        boolmask = np.ones((self.height, self.width), dtype=np.bool)
        j = np.argmin(energy[-1])
        for i in range(self.height-1, -1, -1):
            boolmask[i, j] = False
            j = backtrack[i, j]

        return boolmask

    def remove_seam(self, boolmask):
        boolmaskfilter = np.stack([boolmask] * 3, axis=2)
        return self.image[boolmaskfilter].reshape((self.height, self.width - 1, 3))


    def visualize(self, boolmask,filename,rotate):
        img = self.image
        enr = self.energy
        if rotate:
            img = np.rot90(img,rotate)
            enr = np.rot90(enr,rotate)
            boolmask = np.rot90(boolmask,rotate)

        mask = np.zeros(img.shape[0:2])
        alphas = np.zeros(img.shape[0:2])
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if boolmask[i, j] == False:
                    mask[i, j] = 1
                    alphas[i,j]=1.0
        

        norm2 = normalize(enr)

        fig,ax = plt.subplots(2)
        ax[0].imshow(img)
        ax[0].imshow(mask, alpha=alphas, cmap='Reds')

        
        ax[1].imshow(norm2)
        ax[1].imshow(mask, alpha=alphas, cmap='Reds')
        fig.savefig(filename)
