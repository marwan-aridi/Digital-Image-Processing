import numpy as np

class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        # this will initialize a Gaussian filter matrix with zeros
        g_filter = np.zeros((5, 5))
        sigma = 1
        rowIndex = 0
        # Fill the Gaussian filter matrix
        for i in range(-2, 3):
            columnIndex = 0  #this line will reset column index at the start of each row
            for j in range(-2, 3):
                exponent = -1 * (i ** 2 + j ** 2) / (2 * sigma ** 2)
                coefficient = 1 / (2 * np.pi * sigma ** 2)
                g_filter[rowIndex][columnIndex] = coefficient * np.exp(exponent)
                columnIndex += 1
            rowIndex += 1
        return g_filter

    def get_laplacian_filter(self):
        # this will define the Laplacian filter kernel explicitly
        kernel = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
        l_filter = np.array(kernel)
        return l_filter

    def filter(self, filter_name):
        # Get image dimensions
        rows, cols = self.image.shape
        # this will generate a copy of the image to apply the filter on
        input_image = self.image.copy()
        # this will initialize the result image array
        result_image = np.zeros((rows, cols))

        if filter_name == "gaussian":
            # Applying the Gaussian filter
            total = 0
            gaussian_filter = self.get_gaussian_filter()
            filter_rows, filter_cols = gaussian_filter.shape
            # Preparing a padded version of the image
            padded_image = np.zeros((rows + 2 * (filter_rows - 1), cols + 2 * (filter_cols - 1)))
            # it will fill in the padded image
            for i in range(filter_rows - 1, rows + filter_rows - 1):
                for j in range(filter_cols - 1, cols + filter_cols - 1):
                    padded_image[i][j] = input_image[i - (filter_rows - 1)][j - (filter_cols - 1)]
            # Convolve the padded image with the Gaussian filter
            for i in range(rows):
                for j in range(cols):
                    total = sum(gaussian_filter[m][n] * padded_image[i + m][j + n]
                                for m in range(filter_rows) for n in range(filter_cols))
                    result_image[i][j] = total

        elif filter_name == "laplacian":
            # Applying the Laplacian filter
            total = 0
            laplacian_filter = self.get_laplacian_filter()
            filter_rows, filter_cols = laplacian_filter.shape
            # Preparing a padded version of the image
            padded_image = np.zeros((rows + 2 * (filter_rows - 1), cols + 2 * (filter_cols - 1)))
            # it will fill in the padded image
            for i in range(filter_rows - 1, rows + filter_rows - 1):
                for j in range(filter_cols - 1, cols + filter_cols - 1):
                    padded_image[i][j] = input_image[i - (filter_rows - 1)][j - (filter_cols - 1)]
            # Convolve the padded image with the Laplacian filter
            for i in range(rows):
                for j in range(cols):
                    total = sum(laplacian_filter[m][n] * padded_image[i + m][j + n]
                                for m in range(filter_rows) for n in range(filter_cols))
                    result_image[i][j] = total

        return result_image