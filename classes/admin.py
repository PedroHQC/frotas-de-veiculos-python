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

    def searchDriver(self,searchData, driverDb):
        for i in driverDb:
            if i.CPF == searchData:
                return i

    def deleteDriver(self, driverData, driverDb):
        driverDb = self.searchDriver(driverData, driverDb)

        if driverDb == None:
            return
        
        driverDb.remove(driverDb)

    def registerVeicle(self, veicleDb):

        brand = str(input("Digite a marca do veiculo: "))
        model = str(input("Digite o modelo do veiculo: "))
        year = str(input("Digite o ano do veiculo: "))
        plate = str(input("Digite a placa"))
        chassis = str(input("Digite o chassi"))
        color = str(input("Digite a cor: "))
        mileage =  str(input("Digite a quilometragem: "))

        veicleDb.append((veicle(brand,model,year,plate,chassis,color,mileage)))

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
    
    def registrySuply(self, suplyDb):
        suplyDb.append(suply(str(input("Digite a data do reabastecimento: ")), str(input("Digite a quantidade de combustivel abastecido: ")), str(input("Digite o valor cobrado: ")), self.searchVeicle(str(input("digite a ")))))
