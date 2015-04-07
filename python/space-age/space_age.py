
EARTH_YEAR_SECS = 31557600
YEAR_SECONDS = {
    "EARTH": EARTH_YEAR_SECS,
    "MERCURY": 0.2408467*EARTH_YEAR_SECS,
    "VENUS": 0.61519726*EARTH_YEAR_SECS,
    "MARS": 1.8808158*EARTH_YEAR_SECS,
    "JUPITER": 11.862615*EARTH_YEAR_SECS,
    "SATURN": 29.447498*EARTH_YEAR_SECS,
    "URANUS": 84.016846*EARTH_YEAR_SECS,
    "NEPTUNE": 164.79132*EARTH_YEAR_SECS,    
}


class SpaceAge:
    def __init__(self, age_sec):
        self._age_in_sec = age_sec

    @classmethod
    def _divide_float(cls, l, r, precision=2):
        return round(l/r,precision)
	
    @property
    def seconds(self):
        return self._age_in_sec
	
    def on_earth(self):
        return self._divide_float( self.seconds, YEAR_SECONDS["EARTH"])
	
    def on_mercury(self):
        return self._divide_float( self.seconds, YEAR_SECONDS["MERCURY"])
	
    def on_venus(self):
        return self._divide_float( self.seconds, YEAR_SECONDS["VENUS"])

    def on_mars(self):
       return self._divide_float( self.seconds, YEAR_SECONDS["MARS"])
	
    def on_jupiter(self):
        return self._divide_float( self.seconds, YEAR_SECONDS["JUPITER"])
	
    def on_saturn(self):
        return self._divide_float( self.seconds, YEAR_SECONDS["SATURN"]) 
	
    def on_uranus(self):
        return self._divide_float( self.seconds, YEAR_SECONDS["URANUS"])
	
    def on_neptune(self):
        return self._divide_float( self.seconds, YEAR_SECONDS["NEPTUNE"])
	

