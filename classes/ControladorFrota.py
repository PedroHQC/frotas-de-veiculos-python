from Driver import Driver 
from Veicle import Veicle
from Admin import Admin
from Suply import Suply
from Maintainance import Maintainance

class ControladorFrota:
    def __init__(self, admin: Admin):
        self.disponivel = [i for i in range(admin.veicle)]
        self.indisponivel = []
     
    def alocarVeicleByDriver(driver: Driver, veicle: Veicle):
        pass

    def programarManutencao(self, maintainanceDb, veicleDb):
        veicleData = self.searchVeicle(str(input("Digite a placa do veiculo: ")), veicleDb)
        date = str(input("Digite a data da manutenção: "))
        mType = str(input("Digite o tipo da manutanção: "))
        cost = float("Digite o valor da manutenção: ")
        
        maintainanceDb.append(Maintainance(veicleData, date, mType, cost))

    def programarAbastecimento():
        pass

    def programadorViagem(driver: Driver, veicle: Veicle):
        pass

