from veicle import veicle
from driver import Driver

class Trip:
    def __init__(self,tripDate, origin, destiny, distance, tripDriver: Driver, tripVeicle: veicle) -> None:
        self.tripDate = tripDate
        self.origin = origin
        self.destiny = destiny
        self.distance = distance
        self.tripDriver = tripDriver
        self.tripVeicle = tripVeicle