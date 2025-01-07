import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def flip(self, image, direction="horizontal"): #defining flip to have a default direction of horizontal image

        if direction == "vertical": #if it is vertical, reverse the rows to flip vertically (veritcal image)
            targetImage = image[::-1, :]

        elif direction == "horizontal": #if it is horizontal, reverse the rows to flip horizontally (veritcal image)
            targetImage = image[:, ::-1]

        else: #nothing to show here, pass to "return target image"
            pass

        return targetImage


        return image



    def chroma_keying(self, foreground, background, target_color, threshold):

        rowCount = foreground.shape[0] #this line to is get the num of rows
        columnCount = foreground.shape[1]#this line to is get the num of columns
        targetImage = zeros((rowCount, columnCount, 3), dtype ="uint8") #this line is to create an empty image array with the same size as foreground

        #this is a nested for loops to rows and columns in the image
        for r in range(rowCount):
            for c in range(columnCount):
                distance = sqrt(sum((foreground[r, c] - target_color) ** 2)) #Euclidean distance
                targetImage[r, c] = (background if distance < threshold else foreground)[r, c]
                #line 41 is to assign current pixel from the background picture if the distance is less than the threshold .If not, the code will use pixel from the foreground image



        return targetImage #return the target image


        return  foreground