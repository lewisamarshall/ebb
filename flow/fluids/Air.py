from .Fluid import Fluid
from .. import ur

class Air(Fluid):

    @classmethod
    def viscosity(self, temperature=None, pressure=None):
        return ur.pascal * ur.second * 18e-6

    @classmethod
    def density(self, temperature=None, pressure=None):
        return ur.gram/ur.liter * 1.225
