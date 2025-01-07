# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

import numpy as np
import math

class Filtering:

    def __init__(self, image):
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        arr_mask = np.ones(shape) #this will initialize max arrays with 1s
        rows, columns = arr_mask.shape
        # the nested for loop below will loop through each row and column to set specific mask values
        for row in range(rows):
            for column in range(columns):
                if 240 < row < 250 and 230 < column < 240:
                    arr_mask[row][column] = 0
                if 227 < row < 237 and 293 < column < 303:
                    arr_mask[row][column] = 0
                if 274 < row < 284 and 208 < column < 218:
                    arr_mask[row][column] = 0
                if 265 < row < 275 and 275 < column < 285:
                    arr_mask[row][column] = 0
        return arr_mask

    def post_process_image(self, image):
        numRow, numCol = image.shape #this line will get the dimensions of the image
        minVal, maxVal = np.min(image), np.max(image)
        scale = 255 / (maxVal - minVal) #this will calculate the scaling factor for contrast stretching
        enhanced_image = np.zeros((numRow, numCol), dtype=np.uint8)
        #the for loop below will apply contrast stretching to each pixel
        for x in range(numRow):
            for y in range(numCol):
                enhanced_image[x][y] = scale * (image[x][y] - minVal)
        return enhanced_image

    def filter(self):
        raw_image = self.image # this will access the image stored in the instance variable
        fft_transformed = np.fft.fft2(raw_image) # compute the 2D Fast Fourier Transform of the image
        centered_fft = np.fft.fftshift(fft_transformed)
        masking = self.get_mask(raw_image.shape) # this will create a mask for the current image shape
        applied_mask = centered_fft * masking #applying the mask to the frequency domain

        ifft_shifted = np.fft.ifftshift(applied_mask) # this will shift the center back to the original position
        reconstructed_image = np.fft.ifft2(ifft_shifted) # create the Inverse FFT to get the filtered spatial domain image
        magnitude_of_fft = np.absolute(centered_fft)
        final_image = np.uint8(self.post_process_image(np.absolute(reconstructed_image)))
        magnitude_of_fft_scaled = np.uint8(np.log(magnitude_of_fft)) * 10 # Scale the log of the FFT magnitude for visibility
        masked_fft_magnitude = np.uint8(np.log(1 + np.absolute(applied_mask))) * 10
        return final_image, magnitude_of_fft_scaled, masked_fft_magnitude
