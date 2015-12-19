from __future__ import print_function, division, absolute_import
from .. import ur, Q

class Fluid(object):

    _default_units = {'temperature': ur.degC,
                      'pressure': ur.bar,
                      }

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

    @classmethod
    def _wrap(self, f):
        """Decorator to check units on temperature and pressure."""
        def wrapper(self, temperature=None, pressure=None):
            temperature = Q(temperature)
            pressure = Q(pressure)

            if temperature.dimensionless:
                temperature *= self._default_units['temperature']
            elif temperature.dimensionality != \
                    self._default_units['temperature'].dimensionality:
                raise RuntimeError('Incompatible units.')

            if pressure.dimensionless:
                pressure *= self._default_units['pressure']
            elif pressure.dimensionality != \
                    self._default_units['pressure'].dimensionality:
                string = 'Incompatible units. {}.dimensionality != {}.dimensonality'
                raise RuntimeError(string.format(pressure,
                                                 self._default_units['pressure']
                                                 )

