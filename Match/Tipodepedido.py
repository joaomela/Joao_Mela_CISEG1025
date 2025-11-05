dict = { "tipo": input("insere o tipo de troca"), 
        "valor": int(input("insere o valor"))}



if dict["tipo"] == "compra":
    print("Compra de",dict["valor"],"€")
elif dict["tipo"] == "venda":
    print("Venda de",dict["valor"],"€")
else:
    print("Pedido desconhecido")
