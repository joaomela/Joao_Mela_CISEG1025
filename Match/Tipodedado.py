valor = input("Introd um dado")

try:
    int(valor)
    print("Número inteiro")

except ValueError:
    try:
        float(valor)
        print("Número decimal")

    except ValueError:
        if valor.startswith("[") and valor.endswith("]"):
            print("lista")
        elif valor.isdigit():
            print("String númerica")
        elif valor.isalpha():
            print("String textual")
        else:
            print("Tipo desconhecido")