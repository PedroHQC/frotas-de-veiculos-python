from veicle import veicle
from driver import driver

class trip:
    def __init__(self, origin, destiny, distance, tripDriver: driver, tripVeicle: veicle) -> None:
        
        self.origin = origin
        self.destiny = destiny
        self.distance = distance
        self.tripDriver = tripDriver
        self.tripVeicle = tripVeicle