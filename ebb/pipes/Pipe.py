from __future__ import division, absolute_import

from contextlib import contextmanager
from ..units import unit_registry as ur

class Pipe(object):
    """A base-class for pipe objects."""

    _fluid = None
    _pressure = None
    _temperature = None
    _length = None

    @property
    def length(self):
        return self._length

    @property
    def hydraulic_diameter(self):
        """Cross-sectional area divided by one-fourth the perimeter."""
        return 4 * self.section / self.perimeter

    def __init__(self):
        raise NotImplementedError

    def __repr__(self):
        """Return an unambiguous string representation."""
        inner = []
        for prop in self.__dict__:
            prop = str(prop)  # convert unicode to string
            value = getattr(self, prop)
            inner.append('{}={}'.format(str(prop).lstrip('_'), str(value)))
        return '{}({})'.format(type(self).__name__, ', '.join(inner))

    def __str__(self):
        """Return a readable string representation."""
        return repr(self)

    def _context(self, fluid, pressure, temperature):
        """Context manager to temporarily set conditions."""
        old_fluid = self.fluid()
        old_pressure = self.pressure()
        old_temperature = self.temperature()

        @contextmanager
        def _contextmanager():
            if fluid is not False:
                self.fluid(fluid)
            if pressure is not False:
                self.pressure(pressure)
            if temperature is not False:
                self.temperature(temperature)

            yield

            self.fluid(old_fluid)
            self.pressure(old_pressure)
            self.temperature(old_temperature)

        return _contextmanager()

    def fluid(self, fluid=False):
        if fluid is not False:
            self._fluid = fluid
        else:
            return self._fluid


    @ur.wraps(None, (ur.bar))
    def pressure(self, pressure=False):
        if pressure is not False:
            self._pressure = pressure
        else:
            return self._pressure

    @ur.wraps(None, (None, ur.degC))
    def temperature(self, temperature=False):
        if temperature is not False:
            self._temeprature = temperature
        else:
            return self._temperature

    def flow(self, fluid=False, pressure=False, temperature=False):
        """The volumetric flow rate of fluid in the channel."""
        with self._context(fluid, pressure, temperature):
            return self._flow().to('L/s')

    def resistance(self, fluid=False, pressure=False, temperature=False):
        """The hydrodynamic resistance of the channel."""
        with self._context(fluid, pressure, temperature):
            return self._resistance()

    def velocity(self, radius, angle, fluid=False,
                 pressure=False, temperature=False):
        with self._context(fluid, pressure, temperature):
            return self._velocity(radius, angle).to('m/s')

    def maximum_velocity(self, fluid=False, pressure=False, temperature=False):
        """The maximum velocity in the pipe."""
        with self._context(fluid, pressure, temperature):
            return self._maximum_velocity().to('m/s')

    def reynolds(self, fluid=False, pressure=False, temperature=False):
        """The non-dimensional ratio of intertial and viscous forces."""
        with self._context(fluid, pressure, temperature):
            return (self.maximum_velocity() *
                    self.hydraulic_diameter /
                    self.fluid().kinematic()).to('')

    @property
    def volume(self):
        """Volume of the pipe."""
        return self.section * self.length

    @property
    def section(self):
        """Cross sectional area of the pipe."""
        return self._section()

    @property
    def perimeter(self):
        """length of line around pipe."""
        return self._perimeter()

    @property
    def surface(self):
        """Surface area of the pipe."""
        return self.perimeter * self.length
