from __future__ import division, print_function, absolute_import
from .. import ur


class Pipe(object):

    _fluid = None
    _pressure = None

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def fluid(self, fluid=False):
        if fluid is not False:
            self._fluid = fluid
        else:
            return self._fluid

    def pressure(self, pressure=False):
        if pressure is not False:
            self._pressure = pressure
        else:
            return self._pressure

    def flowrate(self, pressure, viscosity=None):
        raise NotImplementedError

    def resistance(self, viscosity=None):
        raise NotImplementedError

    @property
    def volume(self):
        return self.section * self.length

    @property
    def section(self):
        raise NotImplementedError

    @property
    def surface(self):
        raise NotImplementedError
