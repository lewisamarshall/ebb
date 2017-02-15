from .Gas import Gas
from ..units import Quantity as Q

class Oxygen(Gas):

    molecular_weight = Q('36 grams/mol')
    reference_viscosity = Q('20.18 uPa s')
    reference_temperature = Q('292.25 K')
    sutherland = Q('127 K')
