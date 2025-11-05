n1 = int(input("Escreve o n1"));
n2 = int(input("Escreve o n2"));
n3 = int(input("Escreve o n3"));

maior = n1;
menor = n1;

if n2 > maior:
    maior=n2
if n3 > maior:
    maior=n3

if n2 < menor:
    menor=n2
if n3 < menor:
    menor=n3

if maior == n1:
    if n2 > n3:
        meio=n2
    elif n3 > n2:
        meio=n3
if maior == n2:
    if n1 > n3:
        meio=n1
    elif n3 > n1:
        meio=n3
if maior == n3:
    if n2 > n1:
        meio=n2
    elif n1 > n2:
        meio=n1

print(f"Crescente: {menor}, {meio}, {maior}" + f"\nDecrescente: {maior}, {meio}, {menor}")