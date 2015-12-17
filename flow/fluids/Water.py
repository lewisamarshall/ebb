from .Fluid import Fluid
from .. import ur

class Water(Fluid):
    @classmethod
    def viscosity(self, temperature=None, pressure=None):
        return None
