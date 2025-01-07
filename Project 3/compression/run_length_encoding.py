from dip import *


class Rle:
    def __init__(self):
        pass

    def encode_image(self, binary_image):
        encoded = []
        run_length, prev_pixel = 0, -1
        flat_img = binary_image.flatten()
        # loops over every pixel in the flattened image
        for pixel in flat_img:
            if prev_pixel == -1: #check if it is first pixel
                prev_pixel = pixel
                run_length += 1
            elif prev_pixel != pixel: #checks for change in pixel
                encoded.append((run_length, prev_pixel))
                prev_pixel = pixel
                run_length = 1
            else:
                if run_length < 255:
                    run_length += 1
                else:
                    encoded.append((run_length, prev_pixel))
                    prev_pixel = pixel
                    run_length = 1
        encoded.append((run_length, prev_pixel))

        return array(encoded)

    # returns the run length encoded image as numpy array

    def decode_image(self, rle_code, height, width):
        img_dim = [height, width]
        reconstructed_img = []
        # loops over each run-length encoded tuple
        for length, pixel_value in rle_code:
            reconstructed_img.extend([pixel_value] * length)

        return array(reconstructed_img).reshape(img_dim)