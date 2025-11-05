nome = input("Nome")
compra = int(input("Compra"))

if compra <= 200.00:
    desconto = float(compra * 0.10)
    cfinal = compra - desconto
elif compra > 200.00 and compra <= 500.00:
    desconto = float(compra * 0.15)
    cfinal = compra - desconto
elif compra > 500.00:
    desconto = float(compra * 0.20)
    cfinal = compra - desconto

print("Nome:",nome)
print("Compra:",compra)
print("desconto:",desconto)
print("Total:",cfinal)

