n = []

for i in range(10):
    numero = int(input(f"Digita numero {i+1}"))
    n.append(numero)
par = 0
impar = 0


for numero in n:
    if (numero%2) == 0:
        par += 1
    else: 
        impar += 1 

print("Pares:",par,"\nImpares:",impar)