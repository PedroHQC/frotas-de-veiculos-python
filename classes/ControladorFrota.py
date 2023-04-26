from Driver import Driver 
from Veicle import Veicle
from Admin import Admin

class ControladorFrota:
    def __init__(self, admin: Admin):
        self.disponivel = [i for i in range(admin.veicle)]
        self.indisponivel = []
    #Veicular motorista com o veiculo 
    def alocarVeicleByDriver(driver: Driver, veicle: Veicle):
        pass

    def programarManutencao():
        pass

    def programarAbastecimento():
        pass

    def programadorViagem(driver: Driver, veicle: Veicle):
        pass

