from __future__ import division, print_function, absolute_import
from math import pi
from .Pipe import Pipe

class CircularPipe(Pipe):

    def __init__(self, radius, length):
        self._radius = radius
        self._length = length

    def velocity(self, radius=0, pressure=None, fluid=None):
        pass

    @property
    def radius(self):
        return self._radius

    @property
    def length(self):
        return self.length

    @property
    def section(self):
        return pi * self.radius**2.

