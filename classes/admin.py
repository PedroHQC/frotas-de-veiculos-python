from driver import Driver
from veicle import Veicle
from suply import Suply 
from menu import Menu
from trip import Trip
from maintainance import Maintainance

class Admin:
    def __init__(self):
        self.drivers = []
        self.veicles = []
        self.trips = []
        self.supplies = []
        self.maintainances = []

    def registerDriver(self):
        name = str(input("Digite o nome do motorista: "))
        cpf = str(input("Digite o CPF do motorista: "))
        rg = str(input("Digite o RG do motorista: "))
        cnh = str(input("Digite a CNH do motorista: "))

        driver = Driver(name, cpf, rg, cnh)
        self.drivers.append(driver)

    def searchDriver(self):
        searchData = str(input("Digite o CPF do motorista, sem pontos: "))
        for driver in self.drivers:
            if driver.cpf == searchData:
                print(f"Nome: {driver.name}\nCPF: {driver.cpf}\nRG: {driver.rg}\nCNH: {driver.cnh}")
                return driver
            
    def editDriver(self, atributeToChange):
        driverToEdit = self.searchDriver()
        if driverToEdit:
            if atributeToChange == "name":
                driverToEdit.name = str(input("Digite o novo nome a ser salvo: "))    
            elif atributeToChange == "cpf":
                driverToEdit.cpf = str(input("Digite o CPF nome a ser salvo: "))  
            elif atributeToChange == "rg":
                driverToEdit.rg = str(input("Digite o RG nome a ser salvo: "))  
            elif atributeToChange == "cnh":
                driverToEdit.cnh = str(input("Digite o CNH nome a ser salvo: "))  
            print("Motorista modificado com sucesso!\n")
        else:
            print("Motorista não encontrado!\n")
            
    def deleteDriver(self):
        driverToRemove = self.searchDriver()

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
        tripDriver = self.searchDriver(str(input("Digite o CPF do motorista: ")), self.drivers)
        tripVeicle = self.searchVeicle(str(input("Digite a placa do veiculo da viagem: ")),self.veicles)

        trip = Trip(tripDate, origin, destiny, distance, tripDriver, tripVeicle)
        self.trips.append(trip)

    def editTrip(self):
        origin = str(input("Digite a origem da viagem: "))
        destiny = str(input("Digite o destino: "))
        date = str(input("Digite a data da viagem: "))

        for trip in self.trips:
            if trip.origin == origin and trip.destiny == destiny and trip.tripDate == date:
                return trip
            
    def checkVeicleMileage(self, veiclePlate, veicleDb):
    
        veicleMileage = self.searchVeicle(veiclePlate, veicleDb) 

        if veicleMileage:
            return veiclePlate.mileage
    
    def registrySuply(self):

        date = str(input("Digite a data do reabastecimento: "))
        amount = str(input("Digite a quantidade de combustivel abastecido: "))
        value = str(input("Digite o valor cobrado: "))
        veicle = self.searchVeicle()
        gastype = str(input("Descrição da manutenção: "))

        suply = Suply(date, amount, value, veicle, gastype)
        self.supplies.append(suply)

    def registryMaintainance(self, maintainanceDb, veicleDb):

        veicleData = self.searchVeicle()
        date = str(input("Digite a data da manutenção: "))
        mType = str(input("Digite o tipo da manutenção: "))
        cost = float("Digite o valor da manutenção: ")
        
        maintainance = Maintainance(veicleData, date, mType, cost)
        maintainanceDb.append(maintainance)
        #teste