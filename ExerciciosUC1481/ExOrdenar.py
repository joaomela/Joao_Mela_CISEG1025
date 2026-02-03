lista = ["banana", "uva", "abacaxi", "laranja", "banana"] 

print(lista[0][0])

for _ in range(len(lista)):
    for i in range(len(lista) - 1):
        if len(lista[i]) > len(lista[i+1]):
            n = len(lista[i+1])
        else:
            n = len(lista[i])
        for j in range(n):
            if ord(lista[i][j]) > ord(lista[i+1][j]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                break
            elif ord(lista[i][j]) < ord(lista[i+1][j]):
                    break
            else:
                 if lista[i] > lista[i+1]:
                      lista[i], lista[i+1] = lista[i+1], lista[i]
                      break
print(lista)

lista = ["Python", "inteligência", "Aprender", "dados", "Rede"]

for _ in range(len(lista)):
    for i in range(len(lista) - 1):
        if len(lista[i]) > len(lista[i+1]):
            n = len(lista[i+1])
        else:
            n = len(lista[i])
        for j in range(n):
            if ord(lista[i][j].lower()) < ord(lista[i+1][j].lower()):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                break
            elif ord(lista[i][j].lower()) > ord(lista[i+1][j].lower()):
                    break
            else:
                 if lista[i].lower() < lista[i+1].lower():
                      lista[i], lista[i+1] = lista[i+1], lista[i]
                      break

print(lista)

palavra = "algoritmo" 

print(palavra)
nova = ""

for i in range(len(palavra)):
    s = max(palavra)
    nova = s + nova
    ind = palavra.index(s)
    palavra = palavra[:ind]+ palavra[ind+1:]
    
print(nova)

lista = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"] 

for _ in range(len(lista)):
    for i in range(len(lista) - 1):
        cont = 0
        cont2 = 0
        for j in range(len(lista[i])):
            if 'a' <= lista[i][j] <= 'z':
                cont+=1
        for c in range(len(lista[i+1])):
            if 'a' <= lista[i+1][c] <= 'z':
                cont2+=1
        if cont > cont2:
            lista[i], lista[i+1] = lista[i+1], lista[i]
        elif cont < cont2:
            continue 
print(lista)

