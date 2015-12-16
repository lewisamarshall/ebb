
from .Fluid import Fluid
import pint

ur = pint.UnitRegistry()

class Air(Fluid):

    @classmethod
    def viscosity(temperature=None, pressure=None):
        return ur.pascal * ur.second * 18e-6

    @classmethod
    def density(temperature=None, pressure=None):
        return ur.gram/ur.liter * 1.225
