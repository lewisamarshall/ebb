import flow
from flow.pipes import RectangularPipe
from flow.fluids import Air

pipe = RectangularPipe(width=1e-3, height=3e-4, length=2e-2)
pipe.resistance()
pipe.resistance(Air)
with pipe.fluid(Air):
    pipe.flow(pressure=0.1)
