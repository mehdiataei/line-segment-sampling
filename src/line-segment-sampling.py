import numpy as np
from sympy import N
from sympy.geometry import Point, Segment


class LineSegmentSampling2D:
    """
    A class to generate line segments in a rectangular domain of
    size lx, ly
    """

    def __init__(self, num_samples, min_length, max_length, lx, ly):
        self.num_samples = num_samples
        self.lx = lx
        self.ly = ly
        self.min_length = min_length
        self.max_length = max_length

    def generateLine(self):

        x1 = np.random.uniform(0, self.lx)
        y1 = np.random.uniform(0, self.ly)

        a = np.random.rand() * 2 * np.pi

        # Sqrt since the cumulative distribution function (CDF) changes linearly

        r = np.sqrt(np.random.uniform(self.min_length, self.max_length))

        x2 = r * np.cos(a) + x1

        if x2 > self.lx:
            x2 = self.lx
        elif x2 < 0:
            x2 = 0

        y2 = r * np.sin(a) + y1
        
        if y2 > self.ly:
            y2 = self.ly
        elif y2 < 0:
            y2 = 0

        line_seg = Segment(Point(x1, y1), Point(x2, y2))

        return line_seg

a = LineSegmentSampling2D(1, 1, 2, 10, 10)
b = a.generateLine()

print(np.sqrt(float(b.points[0][0] - b.points[1][0])
              ** 2 + float(b.points[0][1] - b.points[1][1]) ** 2))
