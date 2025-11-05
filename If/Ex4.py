saldo = int(input("Saldo"))
cheque = int(input("Cheque"))

if cheque > saldo:
    print("O cheque nao pode ser descontado")
else:
    print("Cheque descontado, saldo:",saldo-cheque)