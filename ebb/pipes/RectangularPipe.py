from __future__ import division, print_function, absolute_import
from math import sqrt, pi, cos, cosh, tanh
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

    def _velocity(self, y=0, z=0, precision=11):
        summation = sum(self._velocity_term(y, z, i) for i in range(1, precision, 2))
        return 16 * self.width**2 / self.fluid().viscosity() / pi**3 * \
                summation * -self.pressure() / self.length


    def _velocity_term(self, y, z, i):
        prefactor = (-1)**((i-1)/2)
        first_term = 1 - (cosh(i * pi * z / 2 / self.width) /
                          cosh(i * pi * self.height / 2 / self.width)
                          )
        second_term = cos(i * pi * y / 2 / self.width) / i**3

        return prefactor * first_term * second_term

    def _maximum_velocity(self):
        return self._velocity(self.height/2, self.width/2)

    def _flow(self, precision=11):
        prefactor = 4 * self.width * self.height**3 / 3 / self.fluid().viscosity()
        return prefactor * self.pressure() / self.length * \
                (1 - 192 * self.height / pi**5 / self.width *
                 sum(self._flow_term(i) for i in range(1, precision, 2)
                     )
                 )

    def _flow_term(self, i):
        return tanh(i * pi * self.height / 2/ self.width) / i**5

    def _resistance(self):
        pass
