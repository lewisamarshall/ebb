from __future__ import division, print_function, absolute_import
from math import sqrt
from .Pipe import Pipe

class RectangularPipe(Pipe):

    _height = None
    _width = None

    def __init__(self, height, width, length):
        self._height = height
        self._width = width
        self._length = length

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def _section(self):
        return self.height * self.width

    def _perimeter(self):
        return 2 * (self.height + self.width)

    def _velocity(self, radius=0, angle=None):
        pass
        # return (1 / 4 / self.fluid.viscosity() * self.pressure() /
        #        self.length * (self.radius**2 - radius**2))

    def _maximum_velocity(self):
        return self._velocity(self.height/2, self.width/2)

    def _flow(self):
        pass
        #Q = pi * self.radius**4 * self.pressure() / self.length / 8 / self.fluid.viscosity()
        #return Q

    def _resistance(self):
        pass
