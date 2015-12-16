from __future__ import print_function, division, absolute_import

import pint


class Fluid(object):

    @classmethod
    def viscosity(temperature=None, pressure=None):
        raise NotImplementedError

    @classmethod
    def density(temperature=None, pressure=None):
        raise NotImplementedError

    @classmethod
    def __str__(self):
        pass

    @classmethod
    def __repr__(self):
        pass
