
lista = []
def cripto():
    mensagem = input("Escreve uma mensagem para criptografar.\n")
    while True:
        chave = input("Escreve a chave secreta.\n")
        if chave.strip() == "":
            chave = input("Escreve a chave secreta.\n")
        else:
            break
    soma = 0
    texto = ""
    for char in chave:
        soma+=ord(char)
    
    for letra in mensagem:
        ascii_val = (ord(letra) - 32 + soma) % 95 + 32
        texto += chr(ascii_val)
    lista.append(texto)
def decrypto():
    pos = int(input("Posição da lista para desencriptar\n"))
    chave = input("Escreve a chave secreta.\n")
    soma = 0
    texto = ""
    for char in chave:
        soma+=ord(char)
    
    for letra in lista[pos]:
        ascii_val = (ord(letra) - 32 - soma) % 95 + 32
        texto += chr(ascii_val)
    del lista[pos]
    lista.insert(pos, texto)

while True:
    print("Menu")
    opc = int(input("1 - Encriptar\n2 - Desencriptar\n3 - Listar\n"))

    if opc == 1:
        cripto()
    elif opc == 2:
        decrypto()
    elif opc == 3:
        print(lista)
    else:
        break