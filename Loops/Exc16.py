soma = 0
contador = 0

while contador < 30:
    a = int(input("Digite um número par entre 1 e 50: "))
    if 1 <= a <= 50:
        if a % 2 == 0:
            soma += a
            contador += 1
        else:
            print("Apenas números pares entre 1 e 50.")
    else:
        print("Apenas números pares entre 1 e 50.")

media = soma / 30
print(f"Média: {media}")