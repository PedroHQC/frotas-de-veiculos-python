class Menu:

    @staticmethod
    def menu():
        print('-'*20)
        print("BEM VINDO AO PAK")
        print('-'*20)
        print("[1] Motorista")
        print("[2] Veículo")
        print("[3] Viagem")
        print("[4] Abastercer")
        print("[5] Manutenção")
        print("[6] Relatório")
        print('-'*20)


    @staticmethod
    def motorista_menu():
        print("[1] Cadastrar Motorista")
        print("[2] Pesquisar Motorista")
        print("[3] Editar Motorista")
        print("[4] Deletar Motorista")

    @staticmethod
    def veiculo_menu():
        print("[1] Cadastrar Veículo")
        print("[2] Pesquisar Veículo")
        print("[3] Editar Veículo")
        print("[4] Deletar Veículo")
        print("[5] Ver quilometragem de Veículo")

    @staticmethod
    def viagem_menu():
        print('[1] Cadastrar Viagem')
        print('[2] Editar Viagem')