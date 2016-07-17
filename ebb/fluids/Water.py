from .Liquid import Liquid
from ..units import unit_registry as ur, Quantity as Q

class Water(Liquid):

    # viscosity parameters
    reference_viscosity = Q('2.414e-5 Pa s')
    activation_temperature = Q('247.8 degK')
    temperature_offset = Q('140 degK')

    # density parameters
    reference_density = Q('999.8 g/L')
    reference_pressure = Q('1 bar')
    reference_temperature = Q(0., ur.degC)
    expansion = Q('0.0002 / degK')
    elasticity = Q('2.15e9 Pa')


    @classmethod
    def _viscosity(self, temperature, pressure):
        reduced_temperature = (self.activation_temperature /
                               (temperature - self.temperature_offset))
        return self.reference_viscosity * 10.** reduced_temperature
