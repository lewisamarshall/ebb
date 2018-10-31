from __future__ import division, absolute_import

from ..units import unit_registry as ur
from ..units import reference_pressure, reference_temperature

class Fluid(object):

    _compressible = False

    def __new__(cls, *args, **kwargs):
        raise TypeError('Fluids may not be instantiated.')

    @classmethod
    @ur.wraps(['Pa s'], ['C', 'Pa'])
    def viscosity(self, temperature=None, pressure=None):
        """Return the dynamic viscosity of the fluid."""
        return self._viscosity(temperature, pressure)

    @classmethod
    def _viscosity(self, temperature, pressure):
        raise NotImplementedError

    @classmethod

    @ur.wraps(['kg/L'], ['C', 'Pa'])
    def density(self, temperature=reference_temperature, pressure=reference_pressure):
        """Return the density of the fluid."""
        return self._density(temperature, pressure)

    @classmethod
    def _density(self, temperature, pressure):
        raise NotImplementedError

    @classmethod
    @ur.wraps(['m^2/s'], ['C', 'Pa'])
    def kinematic(self, temperature=None, pressure=None):
        """return the kinematic viscosity of the fluid."""
        density = self.density(temperature, pressure)
        viscosity = self.viscosity(temperature, pressure)
        return viscosity/density

    @classmethod
    def compressible(self):
        return self._compressible
