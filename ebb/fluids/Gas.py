from __future__ import absolute_import, division

from .Fluid import Fluid
from ..constants import gas_constant
from ..units import Quantity as Q

class Gas(Fluid):

    molecular_weight = Q('0 gram/mol')
    reference_viscosity = Q('0 uPa s')
    reference_temperature = Q('0 K')
    sutherland = Q('0 K')
    _compressible = True

    @classmethod
    def _viscosity(self, temperature, pressure):
        """Estimate the viscosity using Sutherland's formula."""
        viscosity = (temperature.to('K') / self.reference_temperature)**(3/2)
        viscosity *= ((self.reference_temperature - self.sutherland) /
                     (temperature.to('K') - self.sutherland))
        return viscosity * self.reference_viscosity

    @classmethod
    def _density(self, temperature, pressure):
        """Estimate the density using the ideal gas law."""
        return pressure * self.molecular_weight/gas_constant/temperature.to('kelvin')
