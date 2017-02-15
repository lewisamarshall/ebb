from .Gas import Gas
from ..units import Quantity as Q

class Air(Gas):

    molecular_weight = Q('29 grams/mol')
    reference_viscosity = Q('18.27 uPa s')
    reference_temperature = Q('291.15 K')
    sutherland = Q('120 K')
