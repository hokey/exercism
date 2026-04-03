"""
Utility class to handle Space Ages
"""


class SpaceAge:
    """
    Class for handling Space Age arithmetic
    """
    planets = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615, 
        "saturn": 29.447498, 
        "uranus": 84.016846, 
        "neptune": 164.79132
    }
    seconds = 0
    earth_seconds = 31557600
    
    def __init__(self, seconds):
        """
        SpaceAge initializer that store seconds

        :param int seconds: Time in seconds
        """
        self.seconds = seconds

    def __getattr__(self, planet_call):
        """
        Lazy factory method for setting up translation calls for the different planets

        :param str planet_call:  Function call for planets with the format "on_<PLANET>"
        :return function: Lazy loaded function to handle the space age determination.
        """
        if planet_call.startswith("on_"):
            planet = planet_call[3:]
            if planet in self.planets:
                def fn():
                    return round(self.seconds / self.planets[planet] / self.earth_seconds, 2)
                return fn
                
