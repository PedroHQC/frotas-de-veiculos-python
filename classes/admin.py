from driver import driver
from veicle import veicle
from suply import suply
from menu import Menu
class admin:
    def registerDriver(self,driversDb ):

        driversDb.append(driver(str(input("Digite o nome do motorista: ")),str(input("Digite o CPF do motorista: ")),str(input("Digite o RG do motorista: ")),str(input("Digite a CNH do motorista: "))))

    def searchDriver(sef,searchData,searchMode, driverDb):
        if searchMode == "1":
            for i in driverDb:
                if i.CPF == searchData:
                    return i
        elif searchMode == "2":
            for i in driverDb:
                if i.CNH == searchData:
                    return i
        else:
            pass

    def deleteDriver(self,driverData, searchMode, driverDb):
        if driverData == self.searchDriver(driverData, searchMode, driverDb).CPf or driverData == self.searchDriver(driverData, searchMode, driverDb).CNH:
            driverDb.remove(self.searchDriver(driverData, searchMode, driverDb))

    def registerVeicle(self, veicleDb):
        veicleDb.append((veicle(str(input("Digite a marca do veiculo: ")),str(input("Digite o modelo do veiculo: ")),str(input("Digite o ano do veiculo: ")),str(input("Digite a placa")),str(input("Digite o chassi")), str(input("Digite a cor: ")), str(input("Digite a quilometragem: ")))))

    def searchVeicle(self, veiclePlate, veicleDb):
        for i in veicleDb:
            if i.plate == veiclePlate:
                return i

    def editVeicle(self, veiclePlate, veicleDb):
        self.searchVeicle(veiclePlate, veicleDb)
        #esperando menu    

    def deleteVeicle(self, veiclePlate,veicleDb):
        veicleDb.remove(self.searchVeicle(veiclePlate, veicleDb))

    def checkVeicleMileage(self, veiclePlate, veicleDb):
        return self.searchVeicle(veiclePlate, veicleDb).mileage
    
    def registrySuply(self, suplyDb):
        suplyDb.append(suply(str(input("Digite a data do reabastecimento: ")), str(input("Digite a quantidade de combustivel abastecido: ")), str(input("Digite o valor cobrado: ")), self.searchVeicle(str(input("digite a ")))))
