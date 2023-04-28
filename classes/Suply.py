from .Veicle import Veicle

class Suply:
    def __init__(self, date, amount, value, veicle: Veicle, gastype) -> None:
        
        self.date = date
        self.amount = amount
        self.value = value 
        self.veicle = veicle
        self.gasType = gastype