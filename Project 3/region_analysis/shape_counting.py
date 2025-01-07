import dip
from dip import *
import math


class ShapeCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        regions = dict()
        label = 0
        for row in range(image.shape[0]):
            for column in range(image.shape[1]):
                if image[row, column] == 255:
                    if image[row, column - 1] == 0 and image[row - 1, column] == 0:
                        regions[(row, column)] = label
                        label = label + 1
                    if image[row, column - 1] == 0 and image[row - 1, column] == 255:
                        regions[(row, column)] = regions[(row - 1, column)]
                    if image[row, column - 1] == 255 and image[row - 1, column] == 0:
                        regions[(row, column)] = regions[(row, column - 1)]
                    if image[row, column - 1] == 255 and image[row - 1, column] == 255:
                        regions[(row, column)] = regions[(row - 1, column)]
                        if regions[(row, column - 1)] != regions[(row - 1, column)]:
                            del regions[(row, column - 1)]
                            regions[(row, column - 1)] = regions[(row - 1, column)]

        region = {}
        for key, value in regions.items():
            region.setdefault(value, []).append(key)

        return region

    def identify_shapes(self, region):
        final_dict = dict()
        for i in region:
            if len(region[i]) > 40:
                info_shape = {}
                num_pixels = len(region[i])
                y_coord = [point[0] for point in region[i]]
                x_coord = [point[1] for point in region[i]]
                yMax, yMin = max(y_coord), min(y_coord)
                xMax, xMin = max(x_coord), min(x_coord)
                final_shape = True
                if abs((xMax - xMin) - (yMax - yMin)) < 3:
                    type_shape = 'c'
                    for point in region[i]:
                        if (yMax, xMax) == point or (yMax, xMin) == point or (yMin, xMax) == point or (
                        yMin, xMin) == point:
                            type_shape = 's'
                else:
                    type_shape = 'e'
                    for point in region[i]:
                        if (yMax, xMax) == point or (yMax, xMin) == point or (yMin, xMax) == point or (
                        yMin, xMin) == point:
                            type_shape = 'r'
                centroid = ((yMax + yMin) / 2, (xMax + xMin) / 2)
                info_shape = {"Region": i,
                              "Centroid (in terms of (y,x))": centroid,
                              "Area": num_pixels, "Shape": type_shape}
                for j in final_dict:
                    distance_x = abs(centroid[1] - final_dict[j]["Centroid (in terms of (y,x))"][1])
                    distance_y = abs(centroid[0] - final_dict[j]["Centroid (in terms of (y,x))"][0])
                    if math.sqrt((distance_x ** 2) + (distance_y ** 2)) < 50:
                        if num_pixels < final_dict[j]["Area"]:
                            final_shape = False
                        else:
                            del final_dict[j]
                            break

                if final_shape:
                    print(info_shape.items())
                    final_dict[i] = info_shape

        return final_dict

    def count_shapes(self, shapes_data):
        circles, ellipses, rectangles, squares = 0, 0, 0, 0
        for all_shapes in shapes_data:
            shape_type = shapes_data[all_shapes]["Shape"]
            if shape_type == 'c':
                circles += 1
            elif shape_type == 'e':
                ellipses += 1
            elif shape_type == 'r':
                rectangles += 1
            elif shape_type == 's':
                squares += 1

        return {
            "circles": circles,
            "ellipses": ellipses,
            "rectangles": rectangles,
            "squares": squares
        }

    def mark_image_regions(self, image, shapes_data):
        letter_img = image.copy()
        for all_shapes in shapes_data:
            centroid_y = round(shapes_data[all_shapes]["Centroid (in terms of (y,x))"][0])
            centroid_x = round(shapes_data[all_shapes]["Centroid (in terms of (y,x))"][1])
            dip.putText(letter_img, shapes_data[all_shapes]["Shape"],
                        (int(centroid_x), int(centroid_y)), dip.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 0), 2, dip.LINE_AA)
        return letter_img