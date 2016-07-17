from .Liquid import Liquid
from .. import ur, Q

class Water(Liquid):

    # viscosity parameters
    reference_viscosity = 2.414e-5 * ur.pascal * ur.second
    activation_temperature = Q(247.8, ur.degK)
    temperature_offset = Q(140, ur.degK)

    # density parameters
    reference_density = 999.8 * ur.g / ur.liter
    reference_pressure = 1. * ur.bar
    reference_temperature = Q(0., ur.degC)
    expansion = 0.0002 / ur.degK
    elasticity = 2.15e9 * ur.pascal


    @classmethod
    def _viscosity(self, temperature, pressure):
        reduced_temperature = (self.activation_temperature /
                               (temperature - self.temperature_offset))
        return self.reference_viscosity * 10.** reduced_temperature
