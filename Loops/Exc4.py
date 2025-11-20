flag = True
while flag:
    nP = 0
    opc=int(input("escreve numero"))
    for i in range(1,opc+1):
        if opc % i == 0:
            nP += 1
    if opc == 1:
        print("Numero 1 so tem 1 divisor nao e primo")
        break
    else:
        if nP == 2:
            print("o numero é primo")
            flag=False
        else:
            print("o numero nao e primo")
        