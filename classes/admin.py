from driver import driver
from veicle import veicle
from suply import suply
from menu import Menu
from trip import trip
from maintainance import maintainance
class admin:

    def registerDriver(self, driversDb):

        name = str(input("Digite o nome do motorista: "))
        cpf = str(input("Digite o CPF do motorista: "))
        rg = str(input("Digite o RG do motorista: "))
        cnh = str(input("Digite a CNH do motorista: "))

        driversDb.append(driver(name,cpf,rg,cnh))

    def searchDriver(self, searchData, driverDb):
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
        for veicle in veicleDb:
            if veicle.plate == veiclePlate:
                return veicle

    def editVeicle(self, veiclePlate, veicleDb):
        veicleToEdit = self.searchVeicle(veiclePlate, veicleDb)

        if veicleToEdit:
            Menu.veicleMenuEdit()
    
    def deleteVeicle(self, veiclePlate, veicleDb):
        veicleToRemove = self.searchVeicle(veiclePlate, veicleDb)

        if veicleToRemove:
            veicleDb.remove(veicleToRemove)
            
    def checkVeicleMileage(self, veiclePlate, veicleDb):
    
        veicleMileage = self.searchVeicle(veiclePlate, veicleDb) 

        if veicleMileage:
            return veiclePlate.mileage
    
    def registrySuply(self, suplyDb):

        date = str(input("Digite a data do reabastecimento: "))
        amount = str(input("Digite a quantidade de combustivel abastecido: "))
        value = str(input("Digite o valor cobrado: "))
        veicle = self.searchVeicle(str(input("digite a ")))
        # gastype

        suplyDb.append(suply(date, amount, value, veicle))

    def registryMaintainance(self, maintainanceDb, veicleDb):

        veicleData = self.searchVeicle(str(input("Digite a placa do veiculo: ")), veicleDb)
        date = str(input("Digite a data da manutenção: "))
        mType = str(input("Digite o tipo da manutanção: "))
        cost = float("Digite o valor da manutenção: ")
        
        maintainanceDb.append(maintainance(veicleData, date, mType, cost))

    def registryTrip(self, tripDb, driverDb, veicleDb):

        tripDate = str(input("Digite a data da viagem: "))
        origin = str(input("Digite o local de inicio da viagem: "))
        destiny = str(input("Digite o destino da viagem: "))
        distance = float(input("Digite a distancia da viagem em km: "))
        tripDriver = self.searchDriver(str(input("Digite o CPF do motorista: ")), driverDb)
        tripVeicle = self.searchVeicle(str(input("Digite a placa do veiculo da viagem: ")),veicleDb)

        tripDb.append(trip(tripDate,origin, destiny, distance, tripDriver, tripVeicle))

    def editTrip(self, tripDb):
        origin = str(input("Digite a origem da viagem: "))
        destiny = str(input("Digite o destino: "))
        date = str(input("Digite a data da viagem: "))

        for trip in tripDb:
            if trip.origin == origin and trip.destiny == destiny and trip.tripDate == date:
                return trip