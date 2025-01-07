import numpy as np

from .interpolation import interpolation
from dip import *
import math

class Distort:
    def __init__(self):
        pass

    def distortion(self, image, k):
        """Applies distortion to the image
                image: input image
                k: distortion Parameter
                return the distorted image"""
        (cx, cy) = (image.shape[0] / 2, image.shape[1] / 2)
        # center = (cx, cy)
        distorted_image = zeros(image.shape, dtype=uint8)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                (ic, jc) = (i - cx, j - cy)
                r = math.sqrt(ic**2 + jc**2)
                (icd, jcd) = (ic/(1+k*r), jc/(1+k*r))
                (i_d, j_d) = (icd + cx, jcd + cy)
                distorted_image[round(i_d), round(j_d)] = image[i, j]
        return distorted_image

    def correction_naive(self, distorted_image, k):
        """Applies correction to a distorted image by applying the inverse of the distortion function
        image: the input image
        k: distortion parameter
        return the corrected image"""
        (cx, cy) = (distorted_image.shape[0] / 2, distorted_image.shape[1] / 2)
        # center = (cx, cy)
        corrected_image = zeros(distorted_image.shape, dtype=uint8)
        for i_d in range(distorted_image.shape[0]):
            for j_d in range(distorted_image.shape[1]):
                (icd, jcd) = (i_d - cx, j_d - cy)
                r = math.sqrt(icd ** 2 + jcd ** 2)
                (ic, jc) = (icd*(1 + k * r), jcd*(1 + k * r))
                (i, j) = (round(ic + cx), round(jc + cy))
                if 0 <= i < corrected_image.shape[0] and 0 <= j < corrected_image.shape[1]:
                    corrected_image[i, j] = distorted_image[i_d, j_d]
        return corrected_image

    def correction(self, distorted_image, k, interpolation_type):
        """Applies correction to a distorted image and performs interpolation
                image: the input image
                k: distortion parameter
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the corrected image"""
        if interpolation_type == "bilinear":
            linear = interpolation()
        (cx, cy) = (distorted_image.shape[0] / 2, distorted_image.shape[1] / 2)
        corrected_image = zeros(shape(distorted_image), dtype=uint8)
        for i in range(corrected_image.shape[0]):
            for j in range(corrected_image.shape[1]):
                (ic, jc) = (i - cx, j - cy)
                r = math.sqrt(ic ** 2 + jc ** 2)
                # (icd, jcd) = (ic / (1 + k * r), jc / (1 + k * r))
                (ic, jc) = (ic / (1 + k * r), jc / (1 + k * r))
                # (i_d, j_d) = (icd + cx, jcd + cy)
                (ic, jc) = (ic + cx, jc + cy)
                if 0 <= i < corrected_image.shape[0] and 0 <= j < corrected_image.shape[1]:
                    if interpolation_type == "bilinear":
                        linear = interpolation()
                        intensity = linear.bilinear_interpolation(distorted_image, ic, jc)
                        corrected_image[i, j] = intensity
                    elif interpolation_type == "nearest_neighbor":
                        (inn, jnn) = (round(ic), round(jc))
                        corrected_image[i, j] = distorted_image[inn, jnn]
        return corrected_image
