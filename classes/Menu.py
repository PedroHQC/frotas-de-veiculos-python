class Menu:

    @staticmethod
    def line():
        print('-'*20)

    @staticmethod
    def menu():
        print("BEM VINDO AO PAK")
        Menu.line()
        print("[1] Gerenciamento de Motorista")
        print("[2] Gerenciamento de Veículo")
        print("[3] Gerenciamento de Viagem")
        print("[4] Registrar Abastecimento")
        print("[5] Registrar Manutenção")
        print("[6] Relatório")
        print("[0] Sair")
        Menu.line()

    @staticmethod
    def driverMenu(admin):

        while True:
            Menu.line()

            print("[1] Cadastrar Motorista")
            print("[2] Pesquisar Motorista")
            print("[3] Editar Motorista")
            print("[4] Deletar Motorista")
            print("[5] Exibir Motoristas")
            print("[0] Sair")
          

            Menu.line()

            option = input("Sua opção: ")

            try:
                option = int(option)

                
                if option == 1:
                    admin.registerDriver()
                    print("Motorista cadastrado com sucesso! \n")

                elif option == 0:
                    print("Saindo ...\n")
                    return

                elif len(admin.drivers) > 0:
                    if option == 2:
                        searchDriver = admin.searchDriver()

                        if searchDriver:
                            Menu.line()
                            print(f"Nome: {searchDriver.name}\nCPF: {searchDriver.cpf}\nRG: {searchDriver.rg}\nCNH: {searchDriver.cnh}")
                            Menu.line()
                        else:
                            print('Motorista não encontrado!\n')

                    elif option == 3:
                        Menu.driverMenuEdit(admin)
                    elif option == 4:
                        admin.deleteDriver()
                        print("Motorista deletado com sucesso!\n")
                    elif option == 5:
                        admin.showDriver()
                else:
                    print("[ERROR] Não existe motorista ou veículo cadastrado\nou opção inválida\n")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.\n")
    
    @staticmethod 
    def driverMenuEdit(admin):
        while True:
            print("O que deseja editar?")
            Menu.line()
            print("[1] Nome")
            print("[2] CPF")
            print("[3] RG")
            print("[4] CNH")
            print("[0] Voltar")
            Menu.line()
            
            option = input("Sua opção: ")

            try:
                option = int(option)
                
                if option == 1:
                    admin.editDriver("name")
                elif option == 2:
                    admin.editDriver("cpf")
                elif option == 3:
                    admin.editDriver("rg")
                elif option == 4:
                    admin.editDriver("cnh")
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")
    

    @staticmethod
    def veicleMenu(admin):
      

        while True:
            print("[1] Cadastrar Veículo")
            print("[2] Pesquisar Veículo")
            print("[3] Editar Veículo")
            print("[4] Deletar Veículo")
            print("[5] Ver quilometragem de Veículo")
            print("[6] Exibir Veículos")
            print("[0] Voltar")
            Menu.line()

            option = input("Sua opção: ")

            try:
                option = int(option)

                if option == 1:
                    admin.registerVeicle()
                elif option == 0:
                    print("Saindo ...")
                    return
                
                elif len(admin.veicles) > 0:
                    if option == 2:
                        searchVeicle = admin.searchVeicle()

                        if searchVeicle:
                            Menu.line()
                            print(f"Marca: {searchVeicle.brand}\nAno: {searchVeicle.year}\nPlaca: {searchVeicle.plate}\nChassi: {searchVeicle.chassis}\nQuilometragem:{searchVeicle.mileage}\n")
                            Menu.line()
                        else:
                            print("Veículo não encontrado!\n")

                    elif option == 3:
                        Menu.veicleMenuEdit()
                    elif option == 4:
                        admin.deleteVeicle()
                    elif option == 5:
                        print(f"Este é o total de Km do veiculo: {admin.checkVeicleMileage()}\n")
                    elif option == 6:
                        admin.showVeicle()
                else:
                    print("[ERROR] Não existe veículo cadastrado ou opção inválida\n")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")

    @staticmethod 
    def veicleMenuEdit(admin):
       

        while True:
            print("O que deseja editar?")
            Menu.line()
            print("[1] Marca")
            print("[2] Modelo")
            print("[3] Ano")
            print("[4] Placa")
            print("[5] Chassi")
            print("[6] Cor")
            print("[7] Quilometragem")
            Menu.line()
            
            option = input("Sua opção: ")

            try:
                option = int(option)

                if option == 1:
                    admin.editVeicle("brand")
                elif option == 2:
                    admin.editVeicle("model")
                elif option == 3:
                    admin.editVeicle("year")
                elif option == 4:
                    admin.editVeicle("plate")
                elif option == 5:
                    admin.editVeicle("chassis")
                elif option == 6:
                    admin.editVeicle("color")
                elif option == 7:
                    admin.editVeicle("mileage")
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")

    @staticmethod
    def tripMenu(admin):

        while True:
            print('[1] Cadastrar Viagem')
            print('[2] Editar Viagem')
            print('[3] Mostrar viagens')
            print('[0] Voltar')
            Menu.line()

            option = input("Sua opção: ")

            try:
                option = int(option)

                if option == 1:
                    admin.registryTrip()
                elif option == 0:
                    print("Saindo ...")
                    return
                elif len(admin.trips) > 0:
                    if option == 2:
                        Menu.tripMenuEdit()
                    elif option == 3:
                        admin.showTrip()
                else:
                    print("[ERROR] Não existe motorista ou veículo cadastrado\nou opção inválida\n")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")
    
    @staticmethod 
    def tripMenuEdit(admin):

        while True:
            print("O que deseja editar?")
            Menu.line()
            print("[1] Data")
            print("[2] Origem")
            print("[3] Destino")
            print("[4] Distancia")
            print("[5] Motorista")
            print("[6] Veiculo")
            print("[0] Voltar")
            Menu.line()
            
            option = input("Sua opção: ")

            try:
                option = int(option)

                if option == 1:
                    admin.editTrip("tripDate")
                elif option == 2:
                    admin.editTrip("origin")
                elif option == 3:
                    admin.editTrip("destiny")
                elif option == 4:
                    admin.editTrip("distance")
                elif option == 5:
                    admin.editTrip("tripDriver")
                elif option == 6:
                    admin.editTrip("tripVeicle")
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")
    
    @staticmethod
    def suplyMenu(admin):
        

        while True:
            print('[1] Cadastrar Abastecimento')
            print('[0] Voltar')
            Menu.line()

            option = input("Sua opção: ")
            
            try:
                option = int(option)

                if option == 1:
                    admin.registrySuply()
                elif option == 0:
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")
                
    @staticmethod
    def maintainanceMenu(admin):


        while True:
            print('[1] Cadastrar Manuntencao')
            print('[0] Voltar')
            Menu.line()

            option = input("Sua opção: ")
            
            try:
                option = int(option)
                if option == 1:
                    admin.registryMaintainance()
                elif  option == 0:
                    return
                else:
                    print("[ERROR] Opção Inválida")
            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")    
                
    @staticmethod
    def relatorioMenu(admin):

        while True:
            print("[1] Quantidade de motorista")
            print("[2] Quantidade de veiculos")
            print("[3] Motorista que mais realizou viagens")
            print("[4] Motorista que mais km percorreu")
            print("[5] Veiculo com maior km")
            print("[6] Total de despesas com abastecimeno")
            print("[7] Total de despesas de manutencao")
            print("[8] Dicionario com as entidades")
            Menu.line()

            option = input("Sua opção: ")

            try:
                option = int(option)

                if option == 1:
                    admin.driversQuantity()
                elif option == 2:
                    admin.veiclesQuantity()
                elif option == 3:
                    admin.showDriverMostTrips()
                elif option == 4:
                    admin.showDriverMileage()
                elif option == 5:
                    admin.showVeicleBiggerMileage()
                elif option == 6:
                    admin.totalSpentsSuply()
                elif option == 7:
                    admin.totalSpentsMaintainance()
                elif option == 8:
                    admin.dictionary()
                elif option == 0:
                    print("Saindo ...\n")
                    return
                else:
                    print("[ERROR] Opção Inválida\n")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.\n")       