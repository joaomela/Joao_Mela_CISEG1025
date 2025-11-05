dict = { "categoria": "", "preço": 0}

dict["categoria"] = input("categoria")
dict["preço"] = int(input("preço"))

if dict["categoria"] == "eletrônico" and dict["preço"] > 1000:
    print("Produto de luxo")
elif dict["categoria"] == "eletrônico" and dict["preço"] <= 1000:
    print("Produto comum")
elif dict["categoria"] == "alimento":
    print("Produto aliemntar")
else: 
    print("Categoria desconhecida")