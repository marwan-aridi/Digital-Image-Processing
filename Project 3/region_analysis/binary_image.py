class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        hist = [0] * 256
        for row in range(image.shape[0]):  # loops over each row in the image.
            for column in range(image.shape[1]):  # loops over each column in the image.
                hist[image[row, column]] += 1
        return hist

    def find_threshold(self, hist):
        threshold = len(hist) / 2
        sum1, sum2, average1, average2, previous_average1, previous_average2 = 0, 0, 0, 0, 0, 0
        while abs(previous_average1 - average1) > 1 or abs(previous_average2 - average2) > 1:
            previous_average1, previous_average2, average1, average2, sum1, sum2 = average1, average2, 0, 0, 0, 0
            for i in range(len(hist)):
                count = hist[i]
                if i < threshold: # calculations for weighted sum and average for the lower partition
                    sum1 += count
                    average1 += i * count
                else:
                    sum2 += count
                    average2 += i * count
            if sum1 > 0:
                average1 /= sum1
            if sum2 > 0:
                average2 /= sum2
            threshold = round((average1 + average2) / 2)
        return threshold # returns the computed threshold value only

    def binarize(self, image, threshold):
        bin_img = image.copy()
        for row in range(bin_img.shape[0]): # loops over each row in the binary image
            for column in range(bin_img.shape[1]): # loops over each column in the binary image
                bin_img[row, column] = 0 if bin_img[row, column] < threshold else 255

        return bin_img # outputs the binarize image