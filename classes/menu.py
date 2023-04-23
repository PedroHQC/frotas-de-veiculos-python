class Menu:
    @staticmethod
    def line():
        print('-'*20)

    @staticmethod
    def menu():
        print("BEM VINDO AO PAK")
        Menu.line()
        print("[1] Motorista")
        print("[2] Veículo")
        print("[3] Viagem")
        print("[4] Abastercer")
        print("[5] Manutenção")
        print("[6] Relatório")
        print("[0] Sair")
        Menu.line()

    @staticmethod
    def motorista_menu():
        while True:
            print("[1] Cadastrar Motorista")
            print("[2] Pesquisar Motorista")
            print("[3] Editar Motorista")
            print("[4] Deletar Motorista")
            print("[0] Sair")
            Menu.line()

            option = input("Sua opção: ")

            try:
                option = int(option)

                
                if option == 1:
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    Menu.motorista_menu_editar()
                elif option == 4:
                    pass
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")
    
    @staticmethod 
    def motorista_menu_editar():
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
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    pass
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")
    

    @staticmethod
    def veiculo_menu():
        while True:
            print("[1] Cadastrar Veículo")
            print("[2] Pesquisar Veículo")
            print("[3] Editar Veículo")
            print("[4] Deletar Veículo")
            print("[5] Ver quilometragem de Veículo")
            Menu.line()

            option = input("Sua opção: ")

            try:
                option = int(option)

                if option == 1:
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    Menu.veiculo_menu_editar()
                elif option == 4:
                    pass
                elif option == 5:
                    pass
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")

    @staticmethod 
    def veiculo_menu_editar():
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
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    pass
                elif option == 5:
                    pass
                elif option == 6:
                    pass
                elif option == 7:
                    pass
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")

    @staticmethod
    def viagem_menu():
        while True:
            print('[1] Cadastrar Viagem')
            print('[2] Editar Viagem')
            Menu.line()

            option = input("Sua opção: ")

            try:
                option = int(option)

                if option == 1:
                    pass
                elif option == 2:
                    Menu.viagem_menu_editar()
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")
    
    @staticmethod 
    def viagem_menu_editar():
        while True:
            print("O que deseja editar?")
            Menu.line()
            print("[1] Origem")
            print("[2] Destino")
            print("[3] Distancia")
            print("[4] Motorista")
            print("[5] Veículo")
            print("[0] Voltar")
            Menu.line()
            
            option = input("Sua opção: ")

            try:
                option = int(option)

                if option == 1:
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    pass
                elif option == 5:
                    pass
                elif option == 0:
                    print("Saindo ...")
                    return
                else:
                    print("[ERROR] Opção Inválida")

            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.")