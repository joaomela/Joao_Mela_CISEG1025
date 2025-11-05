num1 = int(input("Introduz o 1º número: "))
num2 = int(input("Introduz o 2º número: "))
num3 = int(input("Introduz o 3º número: "))

if num1 > num2 and num2 > num3:
    print(f"O maior número é {num1}, o menor número é {num3}")
elif num1 > num3 and num3 > num2:
    print(f"O maior número é {num1}, o menor número é {num2}, o número do meio é {num3}")
elif num2 > num1 and num1 > num3:
    print(f"O maior número é {num2}, o menor número é {num3}, o número do meio é {num1}")
elif num2 > num3 and num3 > num1:
    print(f"O maior número é {num2}, o menor número é {num1}, o número do meio é {num3}")
elif num3 > num2 and num2 > num1:
    print(f"O maior número é {num3}, o menor número é {num1}, o número do meio é {num2}")
elif num3 > num1 and num1 > num2:
    print(f"O maior número é {num3}, o menor número é {num2}, o número do meio é {num1}")
else:
    print("Alguns números eram iguais")
