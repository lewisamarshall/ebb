from __future__ import print_function, absolute_import, division

from math import exp

from .Fluid import Fluid
from .. import ur
from ..constants import gas_constant

class Liquid(Fluid):

    # viscosity parameters
    reference_viscosity = None
    activation_energy = None

    # density parameters
    expansion = None
    reference_temperature = None
    reference_pressure = None
    reference_density = None
    elasticity = None

    @classmethod
    def _viscosity(self, temperature, pressure):
        reduced_energy = (self.activation_energy /
                          (gas_constant * kelvin(temperature))
                          )
        return self._reference_viscosity * exp(reduced_energy)

    @classmethod
    def _density(self, temperature, pressure):
        density = self.reference_density / (1 + self.expansion *
                                            (temperature - self.reference_temperature))
        density = density / (1 - (pressure - self.reference_pressure) /
                             self.elasticity)
        return density
