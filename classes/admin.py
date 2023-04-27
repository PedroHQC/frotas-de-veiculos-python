from Driver import Driver
from Veicle import Veicle
from Suply import Suply
from Menu import Menu
from Trip import Trip
from Maintainance import Maintainance

class Admin:
    def __init__(self):
        self.drivers = []
        self.veicles = []
        self.trips = []

    def registerDriver(self):
        name = str(input("Digite o nome do motorista: "))
        cpf = str(input("Digite o CPF do motorista: "))
        rg = str(input("Digite o RG do motorista: "))
        cnh = str(input("Digite a CNH do motorista: "))

        driver = Driver(name, cpf, rg, cnh)
        self.drivers.append(driver)

    def searchDriver(self, searchData):
        for driver in self.drivers:
            if driver.cpf == searchData:
                return driver
            
    def editDriver(self, searchData):
        driverToEdit = self.searchDriver(searchData)

        if driverToEdit:
            Menu.driverMenuEdit()

    def deleteDriver(self, driverData):
        driverToRemove = self.searchDriver(driverData)

        if driverToRemove:
            self.drivers.remove(driverToRemove)
        

    def registerVeicle(self):

        brand = str(input("Digite a marca do veiculo: "))
        model = str(input("Digite o modelo do veiculo: "))
        year = str(input("Digite o ano do veiculo: "))
        plate = str(input("Digite a placa"))
        chassis = str(input("Digite o chassi"))
        color = str(input("Digite a cor: "))
        mileage =  str(input("Digite a quilometragem: "))

        veicle = Veicle(brand, model, year, plate, chassis, color, mileage)

        self.veicles.append(veicle)

    def searchVeicle(self, veiclePlate):
        for veicle in self.veicles:
            if veicle.plate == veiclePlate:
                return veicle

    def editVeicle(self, veiclePlate):
        veicleToEdit = self.searchVeicle(veiclePlate)

        if veicleToEdit:
            Menu.veicleMenuEdit()
    
    def deleteVeicle(self, veiclePlate):
        veicleToRemove = self.searchVeicle(veiclePlate)

        if veicleToRemove:
            self.veicles.remove(veicleToRemove)
            
    def registryTrip(self):

        tripDate = str(input("Digite a data da viagem: "))
        origin = str(input("Digite o local de inicio da viagem: "))
        destiny = str(input("Digite o destino da viagem: "))
        distance = float(input("Digite a distancia da viagem em km: "))
        # tripDriver = self.searchDriver(str(input("Digite o CPF do motorista: ")), driverDb)
        # tripVeicle = self.searchVeicle(str(input("Digite a placa do veiculo da viagem: ")),veicleDb)

        trip = Trip(tripDate, origin, destiny, distance)
        self.trips.append(trip)

    def editTrip(self):
        origin = str(input("Digite a origem da viagem: "))
        destiny = str(input("Digite o destino: "))
        date = str(input("Digite a data da viagem: "))

        for trip in self.trips:
            if trip.origin == origin and trip.destiny == destiny and trip.tripDate == date:
                return trip
            
    # def checkVeicleMileage(self, veiclePlate, veicleDb):
    
    #     veicleMileage = self.searchVeicle(veiclePlate, veicleDb) 

    #     if veicleMileage:
    #         return veiclePlate.mileage
    
    # def registrySuply(self, suplyDb):

    #     date = str(input("Digite a data do reabastecimento: "))
    #     amount = str(input("Digite a quantidade de combustivel abastecido: "))
    #     value = str(input("Digite o valor cobrado: "))
    #     veicle = self.searchVeicle(str(input("digite a ")))
    #     # gastype

    #     suplyDb.append(suply(date, amount, value, veicle))

    # def registryMaintainance(self, maintainanceDb, veicleDb):

    #     veicleData = self.searchVeicle(str(input("Digite a placa do veiculo: ")), veicleDb)
    #     date = str(input("Digite a data da manutenção: "))
    #     mType = str(input("Digite o tipo da manutanção: "))
    #     cost = float("Digite o valor da manutenção: ")
        
    #     maintainanceDb.append(maintainance(veicleData, date, mType, cost))
