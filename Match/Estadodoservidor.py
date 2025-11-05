dict = { "status": "", "tempo_resposta": 0}
dict["status"] = input("escreve o status")
dict["tempo_resposta"] = int(input("escreve o tempo de resposta"))


if dict["status"] == "ok" and dict["tempo_resposta"] < 201:
    print("Servidor ativo")
elif dict["status"] == "ok" and dict["tempo_resposta"] >= 201:
    print("Servidor lento")
elif dict["status"] == "erro":
    print("Servidor indisponível")
else: 
    print("Estado desconhecido")