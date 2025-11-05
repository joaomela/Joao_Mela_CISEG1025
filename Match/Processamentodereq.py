dict = { "metodo": "", "conteudo": ""}

dict["metodo"] = input("metodo")
dict["conteudo"] =  input("conteudo")

if dict["metodo"] == "GET":
    print("Requisição GET recebida")
elif dict["metodo"] == "POST" and dict["conteudo"]:
    print("Requisição POST com dados válidos")
elif dict["metodo"] == "POST" and not dict["conteudo"]:
    print("Requisição POST sem dados")
else: 
    print("Método não suportado")