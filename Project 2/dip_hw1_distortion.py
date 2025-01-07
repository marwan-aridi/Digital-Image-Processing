"""dip_hw1.py: Starter file to run howework 1"""

__author__      = "Pranav Mantini"
__email__ = "pmantini@uh.edu"
__version__ = "1.0.0"

import math, sys
from dip import namedWindow, imshow, waitKey, imwrite, imread
import numpy as np
from Transform.distortion import Distort


def display_image(window_name, image):
    """A function to display image"""
    namedWindow(window_name)
    imshow(window_name, image)
    waitKey(0)


def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     interpolation method and writes the output image"""

    # Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-k", "--distortion_parameter", dest="k",
                        help="specify the distortion parameter k", metavar="K")
    parser.add_argument("-m", "--interpolation", dest="interpolate",
                        help="specify the interpolation method (nearest_neighbor or bilinear)", metavar="INTERPOLATION METHOD")

    args = parser.parse_args()

    # Load image
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = imread(args.image)

    # Check k argument
    if args.k is None:
        print("Distortion parameter is not provided")
        print("use the -h option to see usage information")
        k = 0.005
    else:
        k = float(args.k)

    # Check interpolate method argument
    if args.interpolate is None:
        print("Interpolation method not specified, using default=nearest_neighbor")
        print("use the -h option to see usage information")
        interpolation = "nearest_neighbor"
    else:
        if args.interpolate not in ["nearest_neighbor", "bilinear"]:
            print("Invalid interpolation method, using default=nearest_neighbor")
            print("use the -h option to see usage information")
            interpolation = "nearest_neighbor"
        else:
            interpolation = args.interpolate

    distortion_object = Distort()

    # Part 1
    distorted_image = distortion_object.distortion(input_image, k)

    # Part 2
    corrected_image_naive = distortion_object.correction_naive(distorted_image, k)

    # Part 3
    corrected_image = distortion_object.correction(distorted_image, k, interpolation)

    # Write output file
    outputDir = 'output/'

    output_image_name = outputDir + image_name + '_distorted_' + str(k) + ".jpg"
    imwrite(output_image_name, distorted_image)

    output_image_name_corrected_naive = outputDir + image_name + '_corrected_naive_' + str(k) + ".jpg"
    imwrite(output_image_name_corrected_naive, corrected_image_naive)

    output_image_name_corrected = outputDir + image_name + '_corrected_' +str(k) + "_"+ interpolation+".jpg"
    imwrite(output_image_name_corrected, corrected_image)


if __name__ == "__main__":
    main()







