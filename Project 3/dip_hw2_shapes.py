"""dip_hw2_shapes.py: Starter file to run howework 1"""
#Example Usage: ./dip_hw2_shapes
from dip import *

from region_analysis import binary_image as bi
from region_analysis import shape_counting as cc
from compression import run_length_encoding as rle
from Shapes import Shapes

matplotlib.use('Agg')

__author__ = "Pranav Mantini"
__email__ = "pmantini@uh.edu"
__version__ = "1.0.0"


def display_image(window_name, image):
    """A function to display image"""
    namedWindow(window_name)
    imshow(window_name, image)
    waitKey(0)


def create_image():
    grid_squares = 10
    size = 1024
    bg_intensity = 50
    shape_intensity = 200
    spread = 12
    input = ones((size, size), uint8) * bg_intensity
    input = uint8(input + random.normal(-10, 5, (size, size)))

    grid_size = size//grid_squares
    shapes_obj = Shapes(grid_size, bg_intensity, shape_intensity, spread)
    shapes = [shapes_obj.get_square, shapes_obj.get_circle, shapes_obj.get_rectangle, shapes_obj.get_ellipse]

    circles, ellipses, rectangles, squares = 0, 0, 0, 0
    for k in range(grid_squares):
        for l in range(grid_squares):
            shape_function = random.choice(shapes)
            if shape_function == shapes_obj.get_circle:
                circles += 1
            elif shape_function == shapes_obj.get_ellipse:
                ellipses += 1
            elif shape_function == shapes_obj.get_rectangle:
                rectangles += 1
            else:
                squares += 1
            start_x, end_x = k * grid_size, (k+1)*grid_size
            start_y, end_y = l * grid_size, (l + 1) * grid_size

            input[start_x:end_x, start_y:end_y] = shape_function()


    ground_truth = {"circles": circles, "ellipses": ellipses, "rectangles": rectangles, "squares": squares}
    return input, ground_truth

def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     interpolation method and writes the output image"""

    input_image, gt = create_image()

    bin_img = bi.BinaryImage()
    hist = bin_img.compute_histogram(input_image)

    output_directory = 'output/shape_counting/'
    output_directory_compress = 'output/Compression/'

    output_image_name = output_directory + "input_image" + ".jpg"
    imwrite(output_image_name, input_image)

    plt.plot(hist)
    plt.savefig(output_directory+"hist.png")

    threshold = bin_img.find_threshold(hist)
    print("Optimal threshold: ", threshold)

    binary_img = bin_img.binarize(input_image, threshold)
    output_image_name = output_directory + "binary_image" + ".jpg"
    imwrite(output_image_name, binary_img)

    shape_count_obj = cc.ShapeCounting()
    regions = shape_count_obj.blob_coloring(binary_img)
    shapes_data = shape_count_obj.identify_shapes(regions)
    shape_count = shape_count_obj.count_shapes(shapes_data)

    print("Groundtruth ==>", gt)
    print("Identified  ==>", shape_count)

    shape_stats_img = shape_count_obj.mark_image_regions(binary_img, shapes_data)
    output_image_name = output_directory + "shape_stats" + ".jpg"
    imwrite(output_image_name, shape_stats_img)


    rle_obj = rle.Rle()
    rle_code = rle_obj.encode_image(binary_img)
    print("-------------- Runlength Code -------------------")
    print(rle_code)

    [height, width] = binary_img.shape
    decoded_image = rle_obj.decode_image(rle_code, height, width)
    output_image_name = output_directory_compress + "decoded_image" + ".jpg"
    imwrite(output_image_name, decoded_image)


if __name__ == "__main__":
    main()







