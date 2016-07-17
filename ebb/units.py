from __future__ import absolute_import

import pint
from pint.errors import DimensionalityError

# Create an ebb copy of the pint UnitRegistry
# Mixing units from different UnitRegistry objects is bad.
unit_registry = pint.UnitRegistry()
Quantity = unit_registry.Quantity

# Create a dictionary of default units.
# Values entered without units are interpreted as this unit.
default_units = {'length': unit_registry.meter,
                 'time': unit_registry.second,
                 'pressure': unit_registry.pascal,
                 'force': unit_registry.newton,
                 'temperature': unit_registry.degK,
                 }

default_value = {'length': Quantity('1 m'),
                 'time': Quantity('1 s'),
                 'pressure': Quantity('1 bar'),
                 'force': Quantity('1 N'),
                 'temperature': Quantity('298 degK'),
                 }

def unitize(arg, dim):
    if arg is None:
        return default_value[dim]
    else:
        arg = Quantity(arg)
        dim = default_units[dim]
        if arg.dimensionless:
            return arg * dim
        elif arg.dimensionality != dim.dimensionality:
            string = 'Incompatible units. {}.dimensionality != {}.dimensonality'
            raise DimensionalityError(string.format(arg, dim))
        else:
            return arg
