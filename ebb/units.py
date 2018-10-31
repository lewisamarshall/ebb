from __future__ import absolute_import

import pint
from pint.errors import DimensionalityError

# Create an ebb copy of the pint UnitRegistry
# Mixing units from different UnitRegistry objects is bad.
unit_registry = pint.UnitRegistry()

unit_registry.autoconvert_offset_to_baseunit = True
Quantity = unit_registry.Quantity

reference_pressure = Quantity('1 bar'),
reference_temperature = Quantity('25 degC'),

default_value = {'length': Quantity('1 m'),
                 'time': Quantity('1 s'),
                 'pressure': Quantity('1 bar'),
                 'force': Quantity('1 N'),
                 'temperature': Quantity('25 degC'),
                 'angle': Quantity('0 deg'),
                 }
