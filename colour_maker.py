__author__ = 'CSU-OSS-RLTea'

import random
from datetime import datetime


class ColourMaker(object):
    def __init__(self, span=10, start_colour=None, end_colour=None):
        """
        Generates a hexadecimal gradient list based on the start and end colours. When the start or end colour  are
        not specified, the constructor assigns random values to them.
        @param span: Color gradient smoothness. The larger the value, the smoother the gradient. Default value is 10.
        @param start_colour: The starting color of the gradient is a list of three elements with decimal values r, g, b.
        @param end_colour: The ending color of the gradient is a list of three elements with decimal values r, g, b.
        """
        random.seed(datetime.now().timestamp())
        if start_colour is None:
            start_colour = ColourMaker.get_random_colour_dec()
        if end_colour is None:
            end_colour = ColourMaker.get_random_colour_dec()
        if isinstance(start_colour, str):
            start_colour = ColourMaker.hex_colour2dec_colour(start_colour)
        if isinstance(end_colour, str):
            end_colour = ColourMaker.hex_colour2dec_colour(end_colour)

        r_value = [start_colour[0] + int(i_r * (end_colour[0] - start_colour[0]) / span) for i_r in range(span)]
        g_value = [start_colour[1] + int(i_g * (end_colour[1] - start_colour[1]) / span) for i_g in range(span)]
        b_value = [start_colour[2] + int(i_b * (end_colour[2] - start_colour[2]) / span) for i_b in range(span)]
        colour_list = list(zip(r_value, g_value, b_value))
        colors_list_hex = ["#%02x%02x%02x" % (c[0], c[1], c[2]) for c in colour_list]
        self.gradient_list = colors_list_hex[:] + colors_list_hex[::-1]
        self.colour_pointer = 0

    def get_colour(self):
        """
        Gets a colour code from the gradient list.
        """
        self.colour_pointer += 1
        self.colour_pointer %= len(self.gradient_list)
        return self.gradient_list[self.colour_pointer]

    @staticmethod
    def get_random_colour_hex():
        """
        Generates random hexadecimal colour.
        @return: str
        """
        random.seed(datetime.now().timestamp())
        colour = "#" + "".join([random.choice("0123456789ABCDEF") for i_h in range(6)])
        return colour

    @staticmethod
    def get_random_colour_dec():
        """
        Generates random hexadecimal colour.
        @return: list
        """
        random.seed(datetime.now().timestamp())
        colour = [random.randint(0, 255) for i_d in range(3)]
        return colour

    @staticmethod
    def hex_colour2dec_colour(hex_colour):
        """
        Converts from a hexadecimal color code to a decimal list.
        @return: decimal list
        """
        hex_colour = hex_colour[1:]
        r = int(hex_colour[0:2], 16)
        g = int(hex_colour[2:4], 16)
        b = int(hex_colour[4:6], 16)
        rgb = [r, g, b]
        return rgb
