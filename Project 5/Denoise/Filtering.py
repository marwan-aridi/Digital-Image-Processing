import dip
from dip import *
class Filtering:

    def __init__(self, image, filter_name, filter_size, var = None):

        self.image = image

        if filter_name == 'arithmetic_mean':
            self.filter = self.get_arithmetic_mean
        elif filter_name == 'geometric_mean':
            self.filter = self.get_geometric_mean
        if filter_name == 'local_noise':
            self.filter = self.get_local_noise
        elif filter_name == 'median':
            self.filter = self.get_median
        elif filter_name == 'adaptive_median':
            self.filter = self.get_adaptive_median

        self.filter_size = filter_size
        self.global_var = var
        self.S_max = 15

    def get_arithmetic_mean(self, roi):
        AriMean = 0 #initializing the sum of elements to zero
        element_num = len(roi)
        # for loop will loop over all the elements in the region
        for i in range(element_num):
            AriMean = AriMean + roi[i]
        AriMean = AriMean/element_num
        return AriMean

    def get_geometric_mean(self, roi):
        GeoMean = 1 #initializing the sum of elements to one
        element_num = len(roi)
        # for loop will loop over all the elements in the region
        for i in range(element_num):
            GeoMean = GeoMean * roi[i]
        GeoMean = GeoMean**(1/element_num) # take the nth root of the product, where n is the number of elements
        return GeoMean

    def get_local_noise(self, roi):
        local_mean = 0
        local_var = 0
        var_sum = 0
        global_var = self.global_var
        element_num = len(roi)

        # Calculate the local mean of the region of interest
        for i in range(element_num):
            local_mean = local_mean + roi[i]
        local_mean = local_mean/element_num

        # Calculate the local variance based on the mean
        for i in range(element_num):
            var_sum = var_sum + (roi[i] - local_mean) ** 2
        local_var = var_sum/element_num

        gXY = roi[len(roi)//2] # this will get the central pixel value of the region
        fXY = gXY - (global_var/local_var)*(gXY-local_mean) # this will calculate the filtered pixel value correcting for noise
        return fXY

    def get_median(self, roi):
        sortRoi = roi
        sortRoi.sort()
        element_num = len(roi)
        median = 0
        if element_num % 2 == 0: #check if the number is even
            median1 = sortRoi[element_num//2]
            median2 = sortRoi[element_num//2 - 1]
            median = (median1 + median2)/2 # this will calculate the average of the middle elements
        else: #check if the number is odd
            median = sortRoi[element_num//2] # middle element in sorted list
        return median

    def get_adaptive_median(self, image_pad, fz, i, j):
        offset = self.S_max - fz
        roi = []
        element_num = len(roi)
        # populate the roi with values from the padded image using the current filter size and calculated offset
        for y in range(fz):
            for x in range(fz):
                roi.append(image_pad[y+i+offset][x+j+offset])
        MinVal = min(roi)
        MaxVal = max(roi)
        MedVal = self.get_median(roi)
        g_xy = roi[element_num//2]
        S_max = self.S_max
        a_1 = MedVal - MinVal
        a_2 = MedVal - MaxVal
        b_1 = g_xy - MinVal
        b_2 = g_xy - MaxVal
        # decision logic for adaptive median filtering
        if a_1 > 0  and a_2 < 0:
            if b_1 > 0  and b_2 < 0:
                return g_xy
            else:
                return MedVal
        else:
            if fz > S_max:
                return MedVal
            else:
                fz = fz + 2
                return self.get_adaptive_median(image_pad, fz, i, j)

    def filtering(self):
        r, c = self.image.shape
        fz = self.filter_size
        s_max = self.S_max
        # Check if the current filter is the adaptive median filter
        if self.filter == self.get_adaptive_median:
            image_pad = []
            for i in range(r + s_max):
                row = []
                for j in range(c + s_max):
                    row.append(0)
                image_pad.append(row)
            # Copy image pixels to the center of the padded image
            for i in range(r):
                for j in range(c):
                    image_pad[i+s_max//2][j+s_max//2] = self.image[i][j]
        else:
            image_pad = []
            for _ in range(r + fz):
                row = []
                for _ in range(c + fz):
                    row.append(0)
                image_pad.append(row)
            for i in range(r):
                for j in range(c):
                    image_pad[i+fz//2][j+fz//2] = self.image[i][j]

        out_image = self.image.copy()
        # Apply the filter to each pixel in the image
        for i in range(r):
            for j in range(c):
                arr1 = []
                for y in range(fz):
                    for x in range(fz):
                        arr1.append(image_pad[y+i][x+j])
                # Apply the selected filter to the roi and store the result in the output image
                if self.filter == self.get_adaptive_median:
                    out_image[i][j] = self.filter(image_pad, fz, i , j)
                else:
                    out_image[i][j] = self.filter(arr1)
        return out_image
