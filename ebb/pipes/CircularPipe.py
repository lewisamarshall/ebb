from __future__ import division, absolute_import
from math import pi
from .Pipe import Pipe
from ..units import unitize

class CircularPipe(Pipe):

    def __init__(self, radius, length):
        self._radius = unitize(radius, 'length')
        self._length = unitize(length, 'length')

    @property
    def radius(self):
        return self._radius

    def _section(self):
        return pi * self.radius**2.

    def _perimeter(self):
        return 2 * pi * self.radius

    def _velocity(self, radius=0, angle=None):
        return (1 / 4 / self.fluid().viscosity() * self.pressure() /
                self.length * (self.radius**2 - radius**2))

    def _maximum_velocity(self):
        return self._velocity(0, 0)

    def _flow(self):
        Q = pi * self.radius**4 * self.pressure() / self.length / 8 / self.fluid().viscosity()
        return Q

    def _resistance(self):
        pass
