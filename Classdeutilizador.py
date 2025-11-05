dict = { "nome": "", "idade": 0, "tipo": ""}
dict["idade"] = int(input("idade"))
dict["tipo"] = input("tipo")
dict["nome"] = input("nome")

if dict["idade"] < 18:
    print("Utilizador menor de idade")
elif dict["tipo"] == "admin":
    print("Administrador")
else:
    print("Utilizador comum")
