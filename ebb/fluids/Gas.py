from __future__ import absolute_import, division

from .Fluid import Fluid
from ..constants import gas_constant
from ..units import Quantity as Q

class Gas(Fluid):
    molecular_weight = Q('0 gram/mol')

    @classmethod
    def _viscosity(self, temperature, pressure):
        return 1

    @classmethod
    def _density(self, temperature, pressure):
        return pressure * self.molecular_weight/gas_constant/temperature.to('kelvin')
