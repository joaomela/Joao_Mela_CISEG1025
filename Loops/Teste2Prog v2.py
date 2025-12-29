def verNumeros():
    cont = 0

    for i in range(0,50):
        
        sairNumeros = ""
        divisores=0
        primo = False
        perfeito = False
        par = False
        divPerfeitos = 0

        number = int(input("Escreve um numero de 1-1000\n"))

        while number < 1 or number > 1000:
            number = int(input("Escreve um numero de 1-1000\n"))
        
        # Conta os divisores possiveis
        for t in range(1,number+1):
            if number % t == 0:
                divisores+=1
                divPerfeitos+=t
        
        # Verifica primo
        if divisores == 2:
            primo = True
        if primo:
            print("O número é primo")
        else:
            print("O número não é primo")

        # Verifica se é perfeito
        if divPerfeitos-number == number:
            perfeito = True
        if perfeito:
            print("O número é perfeito")
        else:
            print("O número nao é perfeito")

        # Verifica se é par ou impar
        if number % 2 == 0:
            par = True
        if par:
            print("O número é par")
        else:
            print("O número é impar")
        
        print("Numero de divisores",divisores)

        cont+=1

        while cont >= 10:
            sairNumeros = input("Queres sair deste programa?(S/N)\n")
            if sairNumeros == "N":
                cont=0
            elif sairNumeros == "S":
                break
            else:
                continue
        if sairNumeros == "S":
            break

def calculadoraSimples():
    cont=0
    sairCalculadora = ""
    while True:
        print("----Calculadora Simples----")

        n1 = int(input("Escreve o primeiro numero entre 1 a 1000\n"))
        while n1 < 1 or n1 > 1000:
            n1 = int(input("Escreve o primeiro numero entre 1 a 1000\n"))

        n2 = int(input("Escreve o segundo numero entre 1 a 1000\n"))
        while n2 < 1 or n2 > 1000:
            n2 = int(input("Escreve o segundo numero entre 1 a 1000\n"))

        print("Soma:",n1+n2)
        print("Subtração:",(n1-n2))
        print("Multiplicação:",n1*n2)
        
        try:
            print("Divisão:",n1/n2)
        except:
            print("Erro")
        cont+=1
        while cont >= 5:
            sairCalculadora = input("Queres sair deste programa?(S/N)\n")
            if sairCalculadora == "S":
                break
            elif sairCalculadora == "N":
                cont=0
            else:
                continue
        if sairCalculadora == "S":
            break

while True:
    print("----Menu----")
    print("Opção 1 - Ver números")
    print("Opção 2 - Calculadora")
    print("Opção 3 - Sair do programa")

    opc = int(input("Escreve a opção\n"))

    if opc == 1:
        verNumeros()
    elif opc == 2:
        calculadoraSimples()
    elif opc == 3:
        break
    else:
        continue


listaMarcas = []
listaModelos = []
def cadastrarNovo():
    if len(listaMarcas) < 100 and len(listaModelos) < 100:
        marca = input("Escreve a marca do carro\n")
        modelo = input("Escreve o modelo do carro\n")

        listaMarcas.append(marca)
        listaModelos.append(modelo)
    else:
        print("Lista cheia!")

def procurarCarro():

    opc = input("Queres procurar por marca ou modelo?\n")

    if opc == "marca":
        opc = input("Qual é a marca que queres procurar?\n")

        for i in range(0,len(listaMarcas)):
            try:
                if opc == listaMarcas[i]:
                    print("\nMarca encontrada:",opc,"\nPosição:",i,"\nConteúdo:",listaMarcas[i],listaModelos[i])
                else:
                    print("Marca não existe!")
            except:
                print("Erro") 

    if opc == "modelo":
        opc = input("Qual é o modelo que queres procurar?\n")

        for i in range(0,len(listaModelos)):

            try:
                if opc == listaModelos[i]:
                    print("\nMarca encontrada:",opc,"\nPosição:",i,"\nConteúdo:",listaMarcas[i],listaModelos[i])
            except:
                print("Erro")

def excluirCarro():
    opc = int(input("Qual é a posição que queres eliminar?\n"))

    try:
        del listaMarcas[opc]
        del listaModelos[opc]
        print("Eliminado com sucesso!")
    except:
        print("Erro")

while True:
    print("\n----Listas----")
    print("1 - introduzir dados")
    print("2 - procura dados")
    print("3 - elimina dados")
    print("4 - Sair do Programa")

    opc = int(input("Escreve a opção\n"))

    if opc == 1:
        cadastrarNovo()
    elif opc == 2:
        procurarCarro()
    elif opc == 3:
        excluirCarro()
    elif opc == 4:
        break