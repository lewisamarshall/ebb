from __future__ import print_function, division, absolute_import
from .. import ur, Q

class Fluid(object):

    _default_units = {'temperature': ur.degK,
                      'pressure': ur.bar,
                      }

    _default_values = {'temperature': Q(25, ur.degC),
                       'pressure': 1 * ur.bar,
                       }

    def __new__(cls, *args, **kwargs):
        raise TypeError('Fluids may not be instantiated.')

    @classmethod
    def viscosity(self, temperature=None, pressure=None):
        """Return the dynamic viscosity of the fluid."""
        temperature = self._unitize(temperature, 'temperature')
        pressure = self._unitize(pressure, 'pressure')
        return self._viscosity(temperature, pressure)

    @classmethod
    def _viscosity(self, temperature, pressure):
        raise NotImplementedError

    @classmethod
    def density(self, temperature=None, pressure=None):
        """Return the density of the fluid."""
        temperature = self._unitize(temperature, 'temperature')
        pressure = self._unitize(pressure, 'pressure')
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

    @classmethod
    def _unitize(self, arg, dim):
        if arg is None:
            return self._default_values[dim]

        arg = Q(arg)
        dim = self._default_units[dim]
        if arg.dimensionless:
            return arg * dim
        elif arg.dimensionality != dim.dimensionality:
            string = 'Incompatible units. {}.dimensionality != {}.dimensonality'
            raise RuntimeError(string.format(arg, dim))
