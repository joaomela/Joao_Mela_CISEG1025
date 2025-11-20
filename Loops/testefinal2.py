def inserir_Cli(ultimo_id):
    nomCli=input("Escreve o nome do cliente\n")
    while nomCli.strip() == "":
        nomCli=input("Escreve o nome do cliente\n")
    moradaCli=input("Escreve a morada do cliente\n")
    while moradaCli.strip() == "":
        moradaCli=input("Escreve a morada do cliente\n")
    telCli=input("Escreve o telemovel do cliente\n")
    while not telCli.isdigit() or telCli.strip() == "":
        telCli=input("Escreve o telemovel do cliente\n")
    nifCli=input("Escreve o nif do cliente\n")
    while not nifCli.isdigit() or len(nifCli) != 9 or nifCli.strip() == "":
        nifCli=input("Escreve o nif do cliente\n")
    while True:
        compraCli = input("Escreve a compra do cliente\n")
        try:
            compraCli = float(compraCli)
            break
        except ValueError:
            print("Valor inválido, tente novamente.")
    if 100 <= compraCli <= 200:
        desconto = 0.05
    elif 200 < compraCli <= 500:
        desconto = 0.1
    elif compraCli > 500:
        desconto = 0.15
    elif 0 < compraCli < 100:
        desconto = 0
    Divfin=compraCli-(compraCli * desconto)
    cliente = {
    "número": ultimo_id,
    "nome": nomCli,
    "morada": moradaCli,
    "telemovel": telCli,
    "nif":  nifCli,
    "compra":   compraCli,
    "Divida Final": Divfin
    }
    return cliente
ultimo_id = 1
lista = []
contador=0
while True:
    print("1. Inserir Cliente")
    print("2. Listar Clientes")
    print("3. Procurar por NumCli")
    print("4. Sair")
    try:
        opc = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Opção inválida")
        continue
    
    if opc == 1:
        lista.append(inserir_Cli(ultimo_id))
        ultimo_id+=1
    elif opc == 2:
        for cliente in lista:
            print(f"Número: {cliente['número']}, Nome: {cliente['nome']}, Morada: {cliente['morada']}, Tel: {cliente['telemovel']}, NIF: {cliente['nif']}, Compra: {cliente['compra']:.2f}, Divida Final: {cliente['Divida Final']:.2f}")
            while True:
                contador=input("Queres ir para o proximo cliente: Sim/Nao\n")
                if contador == "Sim" or contador == "Nao":
                    break
                else:
                    print("Resposta inválida")
            if contador == "Nao":
                break
    elif opc == 3:
        encontrado = False
        try:
            numCliOpc = int(input("Escreve o numero do Cliente que queres ver: "))
        except ValueError:
            print("Número inválido")
            continue
        for cliente in lista:
            if cliente["número"] == numCliOpc:
                print(f"Número: {cliente['número']}, Nome: {cliente['nome']}, Morada: {cliente['morada']}, Tel: {cliente['telemovel']}, NIF: {cliente['nif']}, Compra: {cliente['compra']:.2f}, Divida Final: {cliente['Divida Final']:.2f}")
                encontrado = True
                break
        if not encontrado:
            print("Cliente nao existe")
    elif opc == 4:
        break
    else:
        print("Resposta inválida")