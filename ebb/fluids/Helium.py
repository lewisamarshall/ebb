from .Gas import Gas
from ..units import Quantity as Q

class Helium(Gas):

    molecular_weight = Q('4 grams/mol')
    reference_viscosity = Q('19 uPa s')
    reference_temperature = Q('273 K')
    sutherland = Q('79.4 K')
