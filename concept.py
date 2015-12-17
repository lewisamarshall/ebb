import flow

pipe = flow.RectangularPipe(width=1e-3, height=3e-4, length=2e-2)
pipe.resistance()
pipe.resistance(flow.Air)
with pipe.fluid(flow.Air):
    pipe.flow(pressure=0.1)
