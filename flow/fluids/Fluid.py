from __future__ import print_function, division, absolute_import

class Fluid(object):

    @classmethod
    def viscosity(self, temperature=None, pressure=None):
        raise NotImplementedError

    @classmethod
    def density(self, temperature=None, pressure=None):
        raise NotImplementedError

    @classmethod
    def kinematic(self, temperature=None, pressure=None):
        density = self.density(temperature, pressure)
        viscosity = self.viscosity(temperature, pressure)
        return viscosity/density

    @classmethod
    def __str__(self):
        pass

    @classmethod
    def __repr__(self):
        pass
