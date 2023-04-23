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
        for driver in driverDb:
            if driver.CPF == searchData:
                return driver

    def deleteDriver(self, driverData, driverDb):
        driverToRemove = self.searchDriver(driverData, driverDb)

        if driverToRemove:
            driverDb.remove(driverToRemove)
        

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
        veiclePlate = self.searchVeicle(veiclePlate, veicleDb)

        if veiclePlate == None:
            return
        
        veicleDb.remove(veiclePlate)

    def checkVeicleMileage(self, veiclePlate, veicleDb):
        veiclePlate = self.searchVeicle(veiclePlate, veicleDb) 

        if veiclePlate == None:
            return

        return veiclePlate.mileage
    
    def registrySuply(self, suplyDb):
        suplyDb.append(suply(str(input("Digite a data do reabastecimento: ")), str(input("Digite a quantidade de combustivel abastecido: ")), str(input("Digite o valor cobrado: ")), self.searchVeicle(str(input("digite a ")))))
