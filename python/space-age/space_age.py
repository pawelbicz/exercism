class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self._planets = {
            'on_earth': 31557600,
            'on_mercury': 0.2408467 * 31557600,
            'on_venus': 0.61519726 * 31557600,
            'on_mars': 1.8808158 * 31557600,
            'on_jupiter': 11.862615 * 31557600,
            'on_saturn': 29.447498 * 31557600,
            'on_uranus': 84.016846 * 31557600,
            'on_neptune': 164.79132 * 31557600
        }

    def __getattr__(self, p):
        def calculate():
            return round(self.seconds / self._planets[p], 2)

        if not self._planets[p]:
            raise AttributeError
        return calculate
