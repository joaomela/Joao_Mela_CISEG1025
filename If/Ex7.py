n1 = int(input("Escreve o n1"));
n2 = int(input("Escreve o n2"));
n3 = int(input("Escreve o n3"));

nfinal = ((n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5))

if nfinal >= 6:
    print("APROVADO")
    print(nfinal)

elif nfinal < 6:
    print("REPROVADO")
    print(nfinal)
    