from classes.menu import Menu

def init():
    while True:
        Menu.menu()

        option = input("Sua opção: ")

        try:
            option = int(option)

            if option == 1:
                Menu.motorista_menu()
            elif option == 2:
                Menu.veiculo_menu()
            elif option == 3:
                Menu.viagem_menu()
            elif option == 4:
                pass
            elif option == 5:
                pass
            elif option == 6:
                pass
            elif option == 0:
                print("Saindo ...")
                return
            else:
                print('[ERROR] Opção inválida x/')

        except ValueError:
            print("Opção inválida. Por favor, digite um número válido.")

    

init()