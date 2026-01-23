nome = input("Insere o nome completo:\n")

def validar_input_ascii(nome):

    if not nome:
        print("Nome inválido: campo vazio.")
        return

    # Verificar primeira letra
    if not (65 <= ord(nome[0]) <= 90):
        print("Nome inválido: primeira letra deve ser maiúscula.")
        return

    for i in range(len(nome)):
        ascii_val = ord(nome[i])

        # Verifica se é letra ou espaço
        if not ((65 <= ascii_val <= 90) or (97 <= ascii_val <= 122) or (ascii_val == 32) or (193 <= ascii_val <= 245)):
            print("Nome inválido: contém caracteres não permitidos.")
            return

        # Se for espaço, a próxima letra tem de ser maiúscula
        if ascii_val == 32:
            if not (65 <= ord(nome[i + 1]) <= 90):
                print("Nome inválido: letra após espaço deve ser maiúscula.")
                return

    print("Nome válido!")

validar_input_ascii(nome)
