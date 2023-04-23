class admin:
    def registerDriver(self,driversDb ):

        driversDb.append(driver(str(input("Digite o nome do motorista: ")),str(input("Digite o CPF do motorista: ")),str(input("Digite o RG do motorista: ")),str(input("Digite a CNH do motorista: "))))
    def searchDriver(sef, driverDb):
        pass
        

class driver:
    def __init__(self, name = "Nome não informado", cpf = "CPF não informado", rg = "RG não informado", cnh = "CNH não informado") -> None:
        
        self.name = name
        self.CPF  = cpf
        self.RG = rg
        self.CNH = cnh