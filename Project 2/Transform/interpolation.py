class interpolation:

    def linear_interpolation(self, i, i1, x1, x2, i_d):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).

        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.

        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """
        # Write your code for linear interpolation here
        intensity = i * (x2 - i_d) / (x2 - x1) + i1 * (i_d - x1) / (x2 - x1)
        return intensity

    def bilinear_interpolation(self, image, i_d, j_d):
        """Computes the bilinear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).

        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.

        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensitites I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for bilinear interpolation here
        # Recall that bilinear interpolation performs linear interpolation three times
        # Please reuse or call linear interpolation method three times by passing the appropriate parameters to compute this task
        (x1, y1) = (int(i_d), int(j_d))
        (x2, y2) = (x1 + 1, y1 + 1)
        i11 = image[x1, y1]
        i21 = image[x2, y1]
        i12 = image[x1, y2]
        i22 = image[x2, y2]
        intensity = self.linear_interpolation(i11, i21, x1, x2, i_d)
        # intensity = i11*(x2-i_d)/(x2-x1) + i21*(i_d-x1)/(x2-x1)
        intensity2 = self.linear_interpolation(i12, i22, x1, x2, i_d)
        # intensity2 = i12*(x2-i_d)/(x2-x1) + i22*(i_d-x1)/(x2-x1)
        intensity3 = self.linear_interpolation(intensity, intensity2, y1, y2, j_d)
        # intensity3 = intensity*(y2-j_d)/(y2-y1) + intensity2*(j_d-y1)/(y2-y1)
        return intensity3


