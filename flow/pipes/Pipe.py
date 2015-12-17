


class Pipe(object):

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def flowrate(self, pressure, viscosity=None):
        raise NotImplementedError

    def resistance(self, viscosity=None):
        raise NotImplementedError

    def volume(self):
        raise NotImplementedError

    def section(self):
        raise NotImplementedError

    def surface(self):
        raise NotImplementedError
