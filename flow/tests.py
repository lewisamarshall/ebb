from __future__ import print_function, division, absolute_import

import unittest

from .fluids import Fluid, Air, Water
from .pipes import Pipe, CircularPipe, RectangularPipe

class TestFluid(unittest.TestCase):

    fluid = Fluid

    def test_viscosity(self):
        self.fluid.viscosity()
        self.fluid.viscosity(temperature=30)
        self.fluid.viscosity(pressure=1.5)

    def test_density(self):
        self.fluid.density()
        self.fluid.density(temperature=30)
        self.fluid.density(pressure=1.5)

class TestWater(TestFluid):
    fluid = Water

class TestAir(TestFluid):
    fluid = Air

class TestPipe(unittest.TestCase):
    pipe=Pipe()

    def test_resistance(self):
        self.pipe.resistance(viscosity=1)

    def test_section(self):
        self.pipe.section

    def test_volume(self):
        self.pipe.volume()

class TestCircularPipe(TestPipe):
    pipe=CircularPipe(0.1, 1)

class TestRectangularPipe(TestPipe):
    pipe=RectangularPipe(0.1, 0.05, 1)

if __name__ == '__main__':
    unittest.main()
