from PIL import Image
import numpy as np
import sys
import argparse


from energy_calculators.calculator import EnergyCalculator
from seam_carve.seam_carve import SeamCarve


def show(data):
    image = Image.fromarray(data)
    image.show()


def store(data, path):
    image = Image.fromarray(data)
    image.save(path)


def main(image_path, columns, rows, verbose):
    print("\n============")
    print("image path: ", image_path)
    print("columns to remove: ", columns)
    print("rows to remove: ", rows)
    print("verbose: ", verbose)
    print("============\n")
    cnt = 1

    try:
        image = Image.open(image_path)
    except:
        print("couldn't open image file: ", image_path)

    # np array rgb
    data = np.asarray(image)
    sc = SeamCarve(data)

    print("initial_shape: ", sc.image.shape)

    if rows > 0:
        sc.rotate(1)

        for _ in range(rows):
            boolmask = sc.get_minimum_seam()
            sc.visualize(boolmask, "output/rows_"+str(cnt)+".png", 3)

            if verbose:
                sc.update(sc.remove_seam(boolmask))
                cnt += 1

        sc.rotate(3)

    for _ in range(columns):
        boolmask = sc.get_minimum_seam()
        sc.visualize(boolmask, "output/columns_"+str(cnt)+".png", False)

        if verbose:
            sc.update(sc.remove_seam(boolmask))
            cnt += 1

    print("final shape: ", sc.image.shape)
    print("storing final image to output/final.png")
    store(sc.image,"output/final.png")
    show(sc.image)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        "Remove specified columns and rows from input image.")
    parser.add_argument("-i", metavar='i', type=str,
                        help="image path", required=True)
    parser.add_argument(
        '-c', metavar='i', type=int, help="-c <int> columns to remove, default: 0", default=0)
    parser.add_argument(
        '-r', metavar='i', type=int, help="-r <int> rows to remove, default: 0", default=0)
    parser.add_argument('-v', metavar='v', type=bool,
                        help="-v store each step seam into output directory, default: False",
                        default=False, action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    main(args.i, args.c, args.r, args.v)
