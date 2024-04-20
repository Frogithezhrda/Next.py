class Pixel:

    def __init__(self, x, y, red, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        self._red = 171
        self._blue = 171
        self._green = 171

    def print_pixel_info(self):
        if self._blue == 0 and self._green == 0 and self._red > 1:
            color = "Red"
        elif self._blue == 0 and self._green > 1 and self._red == 0:
            color = "Green"
        elif self._blue > 1 and self._green == 0 and self._red == 0:
            color = "Blue"
        else:
            color = ""
        print(f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) {color}")


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()
