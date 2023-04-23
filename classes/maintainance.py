from veicle import veicle

class maintainance:

    def __init__(self, veicle: veicle, date, maintainanceType, cost) -> None:
        self.veicle = veicle
        self.date = date
        self.maintainanceType = maintainanceType
        self.cost = cost