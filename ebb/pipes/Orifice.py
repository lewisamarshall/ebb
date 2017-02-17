from .Pipe import Pipe
from ..units import unitize
from math import pi, sqrt


class Orifice(Pipe):


    def __init__(self, radius, pipe, length=0):
            self._radius = unitize(radius, 'length')
            self._pipe = unitize(pipe, 'length')
            self._length = unitize(length, 'length')

    @property
    def radius(self):
        return self._radius

    @property
    def pipe(self):
        return self._pipe

    @property
    def length(self):
        return self._length

    def _section(self):
        return pi * self.radius**2.

    @property
    def pipe_section(self):
        return pi * self.pipe**2.


    def _perimeter(self):
        return 2 * pi * self.radius

    def _velocity(self, radius=0, angle=None):
        # TODO: This is not accurate.
        return self.flow()/self.section

    def _maximum_velocity(self):
        # TODO: This is not accurate.
        return self.flow()/self.section

    def _flow(self):
        if self.fluid().compressible():
            raise RuntimeError('No equation for compressible fluids.')
        else:
            flow = self.section
            flow *= (2 * self.pressure() / self.fluid().density())**.5
            flow /= (1-(self.section/self.pipe_section)**2)**.5
            return flow

    def _resistance(self):
        pass
