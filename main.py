from classes.Menu import Menu, Admin


def init():
    admin = Admin()
    while True:
        Menu.menu()

        option = input("Sua opção: ")

        try:
            option = int(option)

            if option == 1:
                Menu.driverMenu(admin)
            elif option == 2:
                Menu.veicleMenu(admin)
            elif option == 3:
                Menu.tripMenu(admin)
            elif option == 4:
                Menu.suplyMenu(admin)
            elif option == 5:
                Menu.maintainanceMenu(admin)
            elif option == 6:
                Menu.relatorioMenu(admin)
            elif option == 0:
                print("Saindo ...")
                return
            else:
                print('[ERROR] Opção inválida x/')

        except ValueError:
            print("Opção inválida. Por favor, digite um número válido.")

    

init()