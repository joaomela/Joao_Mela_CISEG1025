salute = input("escreve um salute")

if salute == "olá" or salute == "bom dia":
    print("Saudação")
elif salute.endswith("?"):
    print("Pergunta")
elif "tchau" in salute or "adeus" in salute:
    print("Despedida")
else:
    print("Mensagem genérica")