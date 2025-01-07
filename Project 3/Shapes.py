from dip import *

class Shapes:
    def __init__(self, grid_size, bg_intensity, shape_intensity, spread):
        self.grid_size = grid_size
        self.bg_avg_intensity = bg_intensity
        self.deviaition = self.bg_avg_intensity // 2

        self.shape_intensity = shape_intensity
        self.spread = spread

    def add_noise(self, image):
        return uint8(image + random.normal(-10, self.spread, (self.grid_size, self.grid_size)))

    def get_ellipse(self):
        background = ones((self.grid_size, self.grid_size), uint8) * self.bg_avg_intensity
        center_coordinates = (self.grid_size // 2, self.grid_size // 2)
        radius = random.randint(self.grid_size // 8, self.grid_size // 4)
        axesLength = (int(radius * 1.5), radius)

        image = ellipse(background, center_coordinates, axesLength, 0, 0, 360, self.shape_intensity, -1)

        return self.add_noise(image)

    def get_circle(self):
        background = ones((self.grid_size, self.grid_size), uint8) * self.bg_avg_intensity
        center_coordinates = (self.grid_size // 2, self.grid_size // 2)
        radius = random.randint(self.grid_size // 8, self.grid_size // 3)

        image = circle(background, center_coordinates, radius, self.shape_intensity, -1)

        return self.add_noise(image)

    def get_square(self):
        background = ones((self.grid_size, self.grid_size), uint8) * self.bg_avg_intensity

        disp_x = random.randint(5, self.grid_size // 4)
        disp_y = random.randint(5, self.grid_size // 4)

        tl = (disp_x, disp_y)

        length = self.grid_size - random.randint(0, self.grid_size // 4) - max(array(tl))

        br = (disp_x + length, disp_y + length)
        image = rectangle(background, tl, br, self.shape_intensity, -1)

        return self.add_noise(image)

    def get_rectangle(self):
        background = ones((self.grid_size, self.grid_size), uint8) * self.bg_avg_intensity

        disp_x = random.randint(3, self.grid_size // 8)
        disp_y = random.randint(3, self.grid_size // 8)
        tl = (disp_x, disp_y)

        width = int(self.grid_size * random.randint(4, 10) / 10)
        length = width * 3
        if random.random() > 0.5:
            br = (disp_x + length, disp_y + width)
        else:
            br = (disp_x + width, disp_y + length)

        image = rectangle(background, tl, br, self.shape_intensity, -1)

        return self.add_noise(image)