from driver import driver
from veicle import veicle
from suply import suply
from menu import Menu

class admin:
    def registerDriver(self,driversDb ):

        name = str(input("Digite o nome do motorista: "))
        cpf = str(input("Digite o CPF do motorista: "))
        rg = str(input("Digite o RG do motorista: "))
        cnh = str(input("Digite a CNH do motorista: "))

        driversDb.append(driver(name,cpf,rg,cnh))

    def searchVeicle(self, veiclePlate, veicleDb):
        for i in veicleDb:
            if i.plate == veiclePlate:
                return i

    def editVeicle(self, veiclePlate, veicleDb):
        veiclePlate = self.searchVeicle(veiclePlate, veicleDb)

        if veiclePlate == None:
            return
        
        Menu.veicleMenuEdit()

        #esperando menu    
    def deleteVeicle(self, veiclePlate,veicleDb):
        veicleDb.remove(self.searchVeicle(veiclePlate, veicleDb))

    def checkVeicleMileage(self, veiclePlate, veicleDb):
        return self.searchVeicle(veiclePlate, veicleDb).mileage
    
    def registrySuply(self, suplyDb, veicleDb):
        suplyDb.append(suply(str(input("Digite a data do reabastecimento: ")),
                            str(input("Digite a quantidade de combustivel abastecido: ")),
                            float(input("Digite o valor cobrado: ")),
                            self.searchVeicle(str(input("Digite a placa do veiculo: ")),veicleDb),
                            str(input("Digite o tipo de combustivel: "))))
    
    def registryMaintainance(self,maintainanceDb, veicleDb):

        veicleData = self.searchVeicle(str(input("Digite a placa do veiculo: ")), veicleDb)
        date = str(input("Digite a data da manutenção: "))
        mType = str(input("Digite o tipo da manutanção: "))
        cost = float("Digite o valor da manutenção: ")
        
        maintainanceDb.append(veicleData, date, mType, cost)

    def registryTrip(self, driverDb, veicleDb):
        origin = str(input("Digite o local de inicio da viagem: "))
        destiny = str(input("Digite o destino da viagem: "))
        distance = float(input("Digite a distancia da viagem em km: "))
        tripDriver = self.searchDriver(str(input("Digite o CPF do motorista: ")),driverDb)
        tripVeicle = self.searchVeicle(str(input("Digite a placa do veiculo da viagem: ")),veicleDb)
