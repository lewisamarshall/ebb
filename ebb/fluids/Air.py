from .Fluid import Fluid
from .Gas import Gas
from ..units import unit_registry as ur, Quantity as Q

class Air(Gas):

    molecular_weight = Q('29 grams/mol')

    @classmethod
    def viscosity(self, temperature=None, pressure=None):
        return ur.pascal * ur.second * 18e-6
