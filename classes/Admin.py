from .Driver import Driver
from .Veicle import Veicle
from .Suply import Suply 
from .Trip import Trip
from .Maintainance import Maintainance
from .Menu import Menu

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
        
    def showDriver(self):
        for driver in self.drivers:
            print(driver.name, driver.cpf)
            

    def deleteDriver(self):
        driverToRemove = self.searchDriver()

        if driverToRemove:
            self.drivers.remove(driverToRemove)
        
    def driversQuantity(self):
        print(f"Esta e a quatidade de motoristas cadastrados: {len(self.drivers)}\n")

    def showDriverMostTrips(self):
        bigger = 0
        for driv in self.trips:
            if len(driv) > len(bigger):
                bigger = driv                
        print(f"O motorista com mais viagens é: {bigger.tripDriver.name}\n")

    def showDriverMileage(self):
        mileage_1 = 0
        mileage_2 = 0
        mileageDriver

        for trips in self.trips:
            for trip in trips:
                mileage_1 += trip.distance
            if mileage_1 > mileage_2:
                mileage_2 = mileage_1
                mileageDriver = trips[0]
            mileage_1 = 0

        print(f"O motorista com maior quilometragem foi: {mileageDriver.tripDriver.name}\n")

    def registerVeicle(self):

        brand = str(input("Digite a marca do veiculo: "))
        model = str(input("Digite o modelo do veiculo: "))
        year = str(input("Digite o ano do veiculo: "))
        plate = str(input("Digite a placa: "))
        chassis = str(input("Digite o chassis: "))
        color = str(input("Digite a cor: "))
        mileage =  str(input("Digite a quilometragem: "))

        veicle = Veicle(brand, model, year, plate, chassis, color, mileage)

        self.veicles.append(veicle)

    def searchVeicle(self):
        veiclePlate = str(input("Digite a placa do motorista, sem pontos: "))

        for veicle in self.veicles:
            if veicle.plate == veiclePlate:
                return veicle

    def editVeicle(self, atributeToChange):
        veicleToEdit = self.searchVeicle()

        if veicleToEdit:
            if atributeToChange == "brand":
                veicleToEdit.brand = str(input("Digite a nova marca a ser salvo: "))    
            elif atributeToChange == "model":
                veicleToEdit.model = str(input("Digite o novo modelo a ser salvo: "))  
            elif atributeToChange == "year":
                veicleToEdit.year = str(input("Digite o novo ano a ser salvo: "))  
            elif atributeToChange == "plate":
                veicleToEdit.plate = str(input("Digite a nova placa a ser salvo: "))  
            elif atributeToChange == "chassis":
                veicleToEdit.chassis = str(input("Digite o novo chassis a ser salvo: "))
            elif atributeToChange == "color":
                veicleToEdit.color = str(input("Digite a nova cor a ser salvo: "))
            elif atributeToChange == "mileage":
                veicleToEdit.mileage = str(input("Digite a nova quilometragem a ser salvo: "))
            print("Motorista modificado com sucesso!\n")
        else:
            print("Motorista não encontrado!\n")

    def deleteVeicle(self):
        veiclePlate = self.searchVeicle()

        veicleToRemove = self.searchVeicle(veiclePlate)

        if veicleToRemove:
            self.veicles.remove(veicleToRemove)

    def showVeicle(self):
        for veicle in self.veicles:
            print(veicle.plate, veicle.model, veicle.chassis)
            
    def checkVeicleMileage(self):
        veicle = self.searchVeicle() 

        if veicle:
            for trip in self.trips:
                if trip.tripVeicle.plate == veicle.plate:
                    veicle.mileage += trip.distance
            
            return veicle.mileage
        
    def veiclesQuantity(self):
        print(f"Esta e a quatidade de veiculos cadastrados: {len(self.veicles)}\n")
       
    def showVeicleBiggerMileage(self):
        biggerMileage = 0
        veicleMostRunned

        for veicle in self.veicles:
            if biggerMileage < self.checkVeicleMileage(veicle.plate):
                biggerMileage = self.checkVeicleMileage(veicle.plate)
                veicleMostRunned = veicle
                
        print(f"Este é a placa do veiculo com maior quilometragem: {veicleMostRunned.plate}\n")

    def registryTrip(self):

        if len(self.veicles) > 0 and len(self.drivers) > 0:

            tripDate = str(input("Digite a data da viagem: "))
            origin = str(input("Digite o local de inicio da viagem: "))
            destiny = str(input("Digite o destino da viagem: "))
            distance = float(input("Digite a distancia da viagem em km: "))
            codTrip = str("Digite o código da viagem: ")
            tripDriver = self.searchDriver()
            tripVeicle = self.searchVeicle()

            trip = Trip(tripDate, origin, destiny, distance, tripDriver, tripVeicle, codTrip)

            self.trips.append(trip)

        else:
            print('[ERROR] Não é possível cadastrar viagem sem motorsista e veículos cadastrados!\n')
            return Menu.menu()
        
    
    def showTrip(self):
        for trip in self.trips:
            print(trip.origin, trip.destiny, trip.tripDriver.name)
    
    def searchTrip(self):
        codTrip = str(input("Digite o codigo da viagem: "))

        for trip in self.trips:
            if trip.codTrip == codTrip:
                return trip
            else:
                print("Viagem não encontrado!")
                return Admin.searchTrip()
            
    def editTrip(self, atributeToChange):
        if len(self.veicles) > 0 and len(self.drivers) > 0:

            tripToEdit = self.searchVeicle()

            if tripToEdit:
                if atributeToChange == "tripDate":
                    tripToEdit.tripDate = str(input("Digite a nova data da viagem: "))    
                elif atributeToChange == "origin":
                    tripToEdit.origin = str(input("Digite a nova origem da viagem: "))  
                elif atributeToChange == "destiny":
                    tripToEdit.destiny = str(input("Digite o novo destino da viagem: "))  
                elif atributeToChange == "distance":
                    tripToEdit.distance = str(input("Digite a nova distancia da viagem: "))  
                elif atributeToChange == "tripDriver":
                    tripToEdit.tripDriver = str(input("Digite o novo motorista da viagem: "))
                elif atributeToChange == "tripVeicle":
                    tripToEdit.tripVeicle = str(input("Digite o novo veiculo da viagem: "))
                print("Informações modificadas com sucesso!\n")
            else:
                print("Informações não encontrado!\n")

        else:
            print('[ERROR] Não é possível cadastrar viagem sem motorsista e veículos cadastrados!\n')
            return Menu.menu()
    
    def registrySuply(self):
        if len(self.veicles) > 0:

            date = str(input("Digite a data do reabastecimento: "))
            amount = str(input("Digite a quantidade de combustivel abastecido: "))
            value = str(input("Digite o valor cobrado: "))
            veicle = self.searchVeicle()
            gastype = str(input("Descrição da manutenção: "))

            suply = Suply(date, amount, value, veicle, gastype)

            self.supplies.append(suply)
        
        else:
            print("[ERROR] Não existe veículo cadastrado!\n")
            return Menu.menu()
        
    def registryMaintainance(self, maintainanceDb, veicleDb):

        veicleData = self.searchVeicle()
        date = str(input("Digite a data da manutenção: "))
        mType = str(input("Digite o tipo da manutenção: "))
        cost = float("Digite o valor da manutenção: ")
        
        maintainance = Maintainance(veicleData, date, mType, cost)

        maintainanceDb.append(maintainance)

    def totalSpentsSuply(self):
        suplySpents = 0
        for suply in self.supplies:
            suplySpents += suply.value
            
        print(f"Este é o gasto total com abastecimentos: {suplySpents}\n")
    
    def totalSpentsMaintainance(self):
        maintainanceSpents = 0
        for maintainance in self.maintainances:
            maintainanceSpents += maintainance.cost
            
        print(f"Este é o gasto total com manutenção: {maintainanceSpents}\n")
    
    def dictionary(self):
        dic = {'Placa': [], 'Código da viagem': [], 'CPF': [], 'Código do Abastecimento': [], 'Código da Manutenção': []}
        for driver in self.drivers:
            dic['CPF'].append(driver['CPF'])
        for veicle in self.veicles:
            dic['Placa'].append(veicle['Placa'])
        for trip in self.trips:
            dic['Código da viagem'].append(trip['Código da viagem'])
        for supply in self.supplies:
            dic['Código do Abastecimento'].append(supply['Código do Abastecimento'])
        for maintenance in self.maintenances:
            dic['Código da Manutenção'].append(maintenance['Código da Manutenção'])
        return dic