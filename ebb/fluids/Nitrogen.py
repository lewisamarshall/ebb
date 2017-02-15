from .Gas import Gas
from ..units import Quantity as Q

class Nitrogen(Gas):

    molecular_weight = Q('28 grams/mol')
    reference_viscosity = Q('17.81 uPa s')
    reference_temperature = Q('300.55 K')
    sutherland = Q('111 K')
