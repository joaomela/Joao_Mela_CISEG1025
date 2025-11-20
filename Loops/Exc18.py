n = int(input("Digite um número: "))
contador = 0

for i in range(1, n + 1):
    soma_divisores = 0
    for j in range(1, i):
        if i % j == 0:
            soma_divisores += j
    if soma_divisores == i:
        print(f"{i} é um número perfeito")
        contador += 1

print(f"Total de números perfeitos entre 1 e {n}: {contador}")