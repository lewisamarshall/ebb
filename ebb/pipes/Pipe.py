from __future__ import division, absolute_import

from contextlib import contextmanager

class Pipe(object):

    _fluid = None
    _pressure = None
    _length = None

    @property
    def length(self):
        return self._length

    @property
    def hydraulic_diameter(self):
        return 4 * self.section / self.perimeter

    def __init__(self):
        raise NotImplementedError

    def __repr__(self):
        """Return an unambiguous string representation."""
        inner = []
        for prop in self.__dict__:
            prop = str(prop).lstrip('_')  # convert unicode to string
            value = getattr(self, prop)
            inner.append('{}={}'.format(str(prop), repr(value)))
        return '{}({})'.format(type(self).__name__, ', '.join(inner))

    def __str__(self):
        """Return a readable string representation."""
        return repr(self)

    def fluid(self, fluid=False):
        if fluid is not False:
            self._fluid, old_fluid = fluid, self._fluid

            @contextmanager
            def fluidmanager():
                yield
                self._fluid = old_fluid

            return fluidmanager()
        else:
            return self._fluid

    def pressure(self, pressure=False):
        if pressure is not False:
            self._pressure, old_pressure = pressure, self._pressure

            @contextmanager
            def pressuremanager():
                yield
                self._pressure = old_pressure

            return pressuremanager()
        else:
            return self._pressure

    def flow(self, pressure=False, fluid=False):
        """The volumetric flow rate of fluid in the channel."""
        with self.fluid(fluid or False), self.pressure(pressure or False):
            return self._flow().to('L/s')

    def resistance(self, fluid=False):
        """The hydrodynamic resistance of the channel."""
        with self.fluid(fluid):
            return self._resistance()

    def velocity(self, radius, angle, pressure=False, fluid=False):
        with self.pressure(pressure), self.fluid(fluid):
            return self._velocity(radius, angle).to('m/s')

    def maximum_velocity(self, pressure=False, fluid=False):
        with self.pressure(pressure), self.fluid(fluid):
            return self._maximum_velocity().to('m/s')

    def reynolds(self, pressure=False, fluid=False):
        with self.fluid(fluid), self.pressure(pressure):
            return (self.maximum_velocity(pressure, fluid) * self.hydraulic_diameter /
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
