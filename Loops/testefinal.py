flag=True
def func_Calc():
    opcOpTab=input("Queres ir para operaçoes ou tabuada(operacao/tabuada)\n")
    if opcOpTab == "operacao":
        vCalc=int(input("nº entre 1 a 1000\n"))
        vCalc2=int(input("nº entre 1 a 1000\n"))
        if 1 <= vCalc <= 1000 and 1 <= vCalc2 <= 1000:
            opcCalc=input("Escolhe \n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão\n")
            if opcCalc == "+":
                print(f"{vCalc} + {vCalc2} = {vCalc + vCalc2}")
            elif opcCalc == "-":
                print(f"{vCalc} - {vCalc2} = {vCalc - vCalc2}")
            elif opcCalc == "*":
                print(f"{vCalc} * {vCalc2} = {vCalc * vCalc2}")
            elif opcCalc == "/":
                print(f"{vCalc} / {vCalc2} = {vCalc / vCalc2}")
            else:
                print("Escolhes-te uma opção inválida")
    elif opcOpTab == "tabuada":
        maxTab = int(input("nº máximo da tabuada?\n"))
        nCalc=-1
        pararCalc = False
        for i in range(1,maxTab+1):
            for t in range(1,maxTab+1):
                nCalc+=1
                if nCalc >= 20:
                    opcCont = input("Mais 20 valores?(sim/nao)\n")
                    nCalc=0
                    if opcCont == "nao":
                        pararCalc = True
                        break
                    elif opcCont == "sim":
                        continue
                    else:
                        print("Resposta inválida")
                        nCalc=20
                        continue
                print(f"{i} * {t} = {i*t}")
            print("")
            if pararCalc == True:
                break
    else:
        print("Resposta inválida")
        return
    
def func_Primo(vAnalise):
    acc=0
    print("Número | Primo | Divisores | Perfeito")
    for i in range(vAnalise,0,-1):
        nDivisores=0
        nPerfeito=0
        sPrimo=False
        nPerfeitoB=False
        for p in range(1,i+1):
            if i % p == 0:
                nDivisores+=1
                if p != i:
                    nPerfeito += p
        if nDivisores == 2:
            sPrimo = True
        if nPerfeito == i:
            nPerfeitoB = True
        print(f"{i:6} | {str(sPrimo):5} | {nDivisores:9} | {nPerfeitoB}")
        acc+=1
        if acc >= 10:
            opcCont = input("Mais 10 valores?(sim/nao)\n")
            if opcCont == "nao":
                break
            else:
                acc=0
                continue

def func_Analise_Num():
    vAnalise = int(input("Nº entre 1 a 30000\n"))
    while vAnalise < 1 or vAnalise > 30000:
        print("Nº nao esta entre o parametro dado")
        vAnalise = int(input("Nº entre 1 a 30000\n"))
    func_Primo(vAnalise)
                
    
while flag:
    print("---Menu---")
    print("1. Analise de numeros")
    print("2. Calculadora simples(+,-,*,/)")
    print("3. Sair")
    opc = input("opçao\n")

    if opc == "1":
        func_Analise_Num()

    if opc == "2":
        func_Calc()
        
    if opc == "3":
        break;    