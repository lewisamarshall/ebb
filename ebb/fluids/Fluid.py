from __future__ import division, absolute_import

from ..units import unitize

class Fluid(object):

    def __new__(cls, *args, **kwargs):
        raise TypeError('Fluids may not be instantiated.')

    @classmethod
    def viscosity(self, temperature=None, pressure=None):
        """Return the dynamic viscosity of the fluid."""
        temperature = unitize(temperature, 'temperature')
        pressure = unitize(pressure, 'pressure')
        return self._viscosity(temperature, pressure)

    @classmethod
    def _viscosity(self, temperature, pressure):
        raise NotImplementedError

    @classmethod
    def density(self, temperature=None, pressure=None):
        """Return the density of the fluid."""
        temperature = unitize(temperature, 'temperature')
        pressure = unitize(pressure, 'pressure')
        return self._density(temperature, pressure)

    @classmethod
    def _density(self, temperature, pressure):
        raise NotImplementedError

    @classmethod
    def kinematic(self, temperature=None, pressure=None):
        """return the kinematic viscosity of the fluid."""
        density = self.density(temperature, pressure)
        viscosity = self.viscosity(temperature, pressure)
        return viscosity/density
