class admin:
    def registerDriver(self,driversDb ):

        driversDb.append(driver(str(input("Digite o nome do motorista: ")),str(input("Digite o CPF do motorista: ")),str(input("Digite o RG do motorista: ")),str(input("Digite a CNH do motorista: "))))
    def searchDriver(sef,searchData,searchMode, driverDb):
        # searchMode = str(input("Digite o tipo de pesquisa:\n1)CPF.\n2)CNH.\n"))
        if searchMode == "1":
            for i in driverDb:
                if i.CPF == searchData:
                    return i
                    # print(f"Motorista encontrado!:\n{i.name}\n{i.CPF}\n{i.RG}\n{i.CNH}")
        if searchMode == "2":
            for i in driverDb:
                if i.CNH == searchData:
                    return i
                    # print(f"Motorista encontrado!:\n{i.name}\n{i.CPF}\n{i.RG}\n{i.CNH}")
        else:
            pass
            # print("Modo de busca invalido!")

    def deleteDriver(self,):
        pass
class driver:
    def __init__(self, name = "Nome não informado", cpf = "CPF não informado", rg = "RG não informado", cnh = "CNH não informado") -> None:
        
        self.name = name
        self.CPF  = cpf
        self.RG = rg
        self.CNH = cnh