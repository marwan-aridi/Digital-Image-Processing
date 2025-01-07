# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries


import math
import numpy as np

class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        rows, columns = matrix.shape #this will get the number of rows and columns from the matrix shape
        output_matrix = np.zeros((rows, columns), dtype=complex) # generate  an output matrix of the same size, initialized with complex zeros
        #the nested for loop below will process each element of the output matrix by applying the forward transformation formula
        for x in range(rows):
            for y in range(columns):
                sum_value = 0
                for i in range(rows):
                    for j in range(columns):
                        angle = 2 * math.pi * (x * i + y * j) / rows
                        complex_expon = complex(math.cos(angle), -math.sin(angle))
                        sum_value += matrix[i][j] * complex_expon
                output_matrix[x][y] = sum_value
        return output_matrix

    def inverse_transform(self, matrix):
        rows, cols = matrix.shape
        output_matrix = np.zeros((rows, cols), dtype=complex)
        # the nested for loop below will compute each element of the output matrix by applying the inverse transformation formula
        for x in range(rows):
            for y in range(cols):
                sum_value = 0
                for i in range(rows):
                    for j in range(cols):
                        angle = 2 * math.pi * (x * i + y * j) / rows
                        complex_expon = complex(math.cos(angle), -math.sin(angle))
                        sum_value += matrix[i][j] * complex_expon
                output_matrix[x][y] = sum_value
        return output_matrix

    def magnitude(self, matrix):
        rows, columns = matrix.shape
        output_matrix = np.zeros((rows, columns))
        #the nested for loop below will calculate the magnitude of each element in the matrix and store in the output matrix
        for i in range(rows):
            for j in range(columns):
                realPart = np.real(matrix[i][j])
                imagPart = np.imag(matrix[i][j])
                output_matrix[i][j] = math.sqrt(realPart ** 2 + imagPart ** 2)
        return output_matrix