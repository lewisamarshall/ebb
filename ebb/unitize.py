from __future__ import absolute_import, print_function, division
from . import ur

def unitize(self, arg, dim):
    if arg is None:
         return self._default_values[dim]

    arg = Q(arg)
    dim = self._default_units[dim]
    if arg.dimensionless:
        return arg * dim
    elif arg.dimensionality != dim.dimensionality:
        string = 'Incompatible units. {}.dimensionality != {}.dimensonality'
        raise RuntimeError(string.format(arg, dim))
