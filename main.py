from classes.Driver import Driver
from classes.Veicle import Veicle
from classes.Suply import Suply 
from classes.Menu import Menu
from classes.Trip import Trip
from classes.Maintainance import Maintainance

def init():
    while True:
        Menu.menu()

        option = input("Sua opção: ")

        try:
            option = int(option)

            if option == 1:
                Menu.driverMenu()
            elif option == 2:
                Menu.veicleMenu()
            elif option == 3:
                Menu.tripMenu()
            elif option == 4:
                Menu.suplyMenu()
            elif option == 5:
                Menu.maintainanceMenu()
            elif option == 6:
                Menu.relatorioMenu()
            elif option == 0:
                print("Saindo ...")
                return
            else:
                print('[ERROR] Opção inválida x/')

        except ValueError:
            print("Opção inválida. Por favor, digite um número válido.")

    

init()