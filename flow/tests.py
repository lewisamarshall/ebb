from __future__ import print_function, division, absolute_import

import unittest

from .fluids import Fluid, Air, Water
from .pipes import Pipe, CircularPipe, RectangularPipe


class FluidTests(object):

    fluid = None

    def test_viscosity(self):
        self.fluid.viscosity()
        self.fluid.viscosity(temperature=30)
        self.fluid.viscosity(pressure=1.5)

    def test_density(self):
        self.fluid.density()
        self.fluid.density(temperature=30)
        self.fluid.density(pressure=1.5)

class TestWater(unittest.TestCase, FluidTests):
    fluid = Water

class TestAir(unittest.TestCase, FluidTests):
    fluid = Air

class TestPipe(object):

    pipe=None

    def test_resistance(self):
        self.pipe.resistance(fluid=Water)

    def test_section(self):
        self.pipe.section

    def test_volume(self):
        self.pipe.volume

    def test_maximum_velocity(self):
        self.pipe.maximum_velocity(fluid=Water, pressure=0.1)

class TestCircularPipe(unittest.TestCase, TestPipe):
    pipe=CircularPipe(0.1, 1)

class TestRectangularPipe(unittest.TestCase, TestPipe):
    pipe=RectangularPipe(0.1, 0.05, 1)

if __name__ == '__main__':
    unittest.main()
