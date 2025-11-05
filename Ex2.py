n1 = int(input("Escreve o n1"));
n2 = int(input("Escreve o n2"));
n3 = int(input("Escreve o n3"));




maior = n1
menor = n1


if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print("Maior:", maior)
print("Menor:", menor)



    
