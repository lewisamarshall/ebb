from __future__ import absolute_import

import unittest

from .fluids import Fluid, Air, Water, Nitrogen, Oxygen, Helium
from .pipes import Pipe, CircularPipe, RectangularPipe, Orifice
from .units import Quantity as Q


class FluidTests(object):

    fluid = Fluid

    def test_compressible(self):
        self.fluid.compressible()

    def test_viscosity(self):
        for viscosity in [self.fluid.viscosity(),
                          self.fluid.viscosity(temperature=30),
                          self.fluid.viscosity(pressure=1.5)]:
            self.assertEqual(viscosity.dimensionality, Q('poise').dimensionality)


    def test_density(self):
        for density in [self.fluid.density(),
                        self.fluid.density(temperature=30),
                        self.fluid.density(pressure=1.5)
                        ]:
            self.assertEqual(density.dimensionality, Q('kg/L').dimensionality)

    def test_kinematic(self):
        for kinematic in [self.fluid.kinematic(),
                          self.fluid.kinematic(temperature=30),
                          self.fluid.kinematic(pressure='1.5 bar')]:
            self.assertEqual(kinematic.dimensionality, Q('poise/kg*L').dimensionality)


class TestWater(unittest.TestCase, FluidTests):
    fluid = Water

class TestAir(unittest.TestCase, FluidTests):
    fluid = Air

class TestNitrogen(unittest.TestCase, FluidTests):
    fluid = Nitrogen

class TestOxygen(unittest.TestCase, FluidTests):
    fluid = Oxygen

class TestHelium(unittest.TestCase, FluidTests):
    fluid = Helium

class TestPipe(object):

    pipe = Pipe
    fluids = (Water, Air)

    def test_resistance(self):
        self.pipe.resistance(fluid=Water)

    def test_section(self):
        self.pipe.section

    def test_volume(self):
        self.pipe.volume

    def test_maximum_velocity(self):
        self.pipe.maximum_velocity(fluid=Water, pressure='0.1 psi')

    def test_flow(self):
        self.pipe.flow(fluid=Water, pressure='0.1 psi')

    def test_reynolds(self):
        self.pipe.reynolds(fluid=Water, pressure='0.1 psi')

class TestUnitedCircularPipe(unittest.TestCase, TestPipe):
    pipe=CircularPipe(Q('1 mm'), Q('1 m'))

class TestUnitedRectangularPipe(unittest.TestCase, TestPipe):
    pipe=RectangularPipe(Q('1 mm'), Q('5 mm'), Q('1 m'))

class TestCircularPipe(unittest.TestCase, TestPipe):
    pipe=CircularPipe(Q('1e-3 m') , Q('1 m'))

class TestRectangularPipe(unittest.TestCase, TestPipe):
    pipe=RectangularPipe(Q('1e-3 m'), Q('5e-3 m'), Q('1 m'))

class TestOrifice(unittest.TestCase, TestPipe):
    pipe = Orifice(Q('1e-4 m'), Q('1e-3 m'))

if __name__ == '__main__':
    unittest.main()
