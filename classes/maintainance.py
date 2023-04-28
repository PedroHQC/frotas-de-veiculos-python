from veicle import Veicle

class Maintainance:

    def __init__(self, veicle: Veicle, date, maintainanceType, cost) -> None:
        self.veicle = veicle
        self.date = date
        self.maintainanceType = maintainanceType
        self.cost = cost