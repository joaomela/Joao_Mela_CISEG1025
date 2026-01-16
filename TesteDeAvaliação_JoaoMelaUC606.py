titulos = []
diretores = []
anoLancamento = []
generos = []

# Insere filmes
def cadastrarFilme():

    filmeExiste = False

    if len(titulos) >= 100:
        print("A capacidade do catálogo é de 100 filmes, neste momento já tem 100 filmes.")
        return
    
    titulo = input("Titulo do filme\n")
    diretor = input("Diretor do filme\n")
    while True:
        try:
            ano = int(input("Ano de lançamento:\n"))
            if 1888 <= ano <= 2026:
                break
            else:
                print("Ano inválido.")
        except ValueError:
            print("Insere um número válido.")
    genero = input("Genero do filme\n")

    
    for i in range(len(titulos)):
        if titulos[i].lower() == titulo.lower() and diretor.lower() == diretores[i].lower():
            print("O filme já existe no catálogo.")
            filmeExiste = True
            break
    if filmeExiste:
        print("Operação não concluida.")
        return
    
    titulos.append(titulo)
    diretores.append(diretor)
    anoLancamento.append(ano)
    generos.append(genero)
    

# Procura filmes
def procurarFilmes():
    filmeEncontrado = False
    print("1 - Procura por Titulo.")
    print("2 - Procura por Diretor.")
    print("3 - Procura por Género.")

    try:

        opc = int(input("Insere o número da opção que queres!\n"))

    except(ValueError):
        print("Erro de valor!")
        return
    if opc == 1:
        tituloProcura = input("Que titulo desejas procurar?\n")

        for i in range(len(titulos)):
            if tituloProcura == titulos[i]:
                print("\nO titulo está no catálogo.")
                print(f"Posição: {i}\ntitulo: {titulos[i]} diretor: {diretores[i]} ano: {anoLancamento[i]} género: {generos[i]}")
                filmeEncontrado = True

        if not filmeEncontrado:
            print("O filme não foi encontrado portanto não está no nosso catálogo.")

    elif opc == 2:
        diretorProcura = input("Qual diretor desejas procurar?\n").lower()
        for i in range(len(diretores)):
            if diretores[i].lower() == diretorProcura:
                print("\nO diretor está no catálogo.")
                print(f"Posição: {i}\ntítulo: {titulos[i]} diretor: {diretores[i]} ano: {anoLancamento[i]} género: {generos[i]}")
                filmeEncontrado = True

    elif opc == 3:
        generoProcura = input("Qual género desejas procurar?\n").lower()
        for i in range(len(generos)):
            if generos[i].lower() == generoProcura:
                print("\nO género está no catálogo.")
                print(f"Posição: {i}\ntítulo: {titulos[i]} diretor: {diretores[i]} ano: {anoLancamento[i]} género: {generos[i]}")
                filmeEncontrado = True

    else:
        print("Opção inexistente.")
        return

    if not filmeEncontrado:
        print("Nenhum filme encontrado para a pesquisa escolhida.")

# Exclui filmes
def excluirFilme():
    try:
        indice = int(input("Qual a posição do filme a excluir?\n"))
        print(f"Filme: {titulos[indice]} - {diretores[indice]}")
    except (ValueError, IndexError):
        print("Índice inválido.")
        return

    confirma = input("Queres realmente excluir? (sim/nao): ").lower()

    if confirma == "sim":
        del titulos[indice]
        del diretores[indice]
        del anoLancamento[indice]
        del generos[indice]
        print("Filme excluído com sucesso.")
    else:
        print("Operação cancelada.")

# Ordena filmes com Bubble sort
def ordenarFilmes():

    if len(titulos) == 0:
        print("Não existem filmes para ordenar.")
        return

    print("Ordenar filmes por:")
    print("1 - Título")
    print("2 - Diretor")
    print("3 - Ano de lançamento")

    try:
        opc = int(input("Escolhe a opção:\n"))
    except ValueError:
        print("Opção inválida.")
        return
    
    n = len(titulos)

    for i in range(n - 1):
        for j in range(n - 1 - i):

            if opc == 1:
                if titulos[j].lower() > titulos[j + 1].lower():

                    titulos[j], titulos[j + 1] = titulos[j + 1], titulos[j]
                    diretores[j], diretores[j + 1] = diretores[j + 1], diretores[j]
                    anoLancamento[j], anoLancamento[j + 1] = anoLancamento[j + 1], anoLancamento[j]
                    generos[j], generos[j + 1] = generos[j + 1], generos[j]

            elif opc == 2:
                if diretores[j].lower() > diretores[j + 1].lower():

                    titulos[j], titulos[j + 1] = titulos[j + 1], titulos[j]
                    diretores[j], diretores[j + 1] = diretores[j + 1], diretores[j]
                    anoLancamento[j], anoLancamento[j + 1] = anoLancamento[j + 1], anoLancamento[j]
                    generos[j], generos[j + 1] = generos[j + 1], generos[j]

            elif opc == 3:
                if anoLancamento[j] > anoLancamento[j + 1]:

                    titulos[j], titulos[j + 1] = titulos[j + 1], titulos[j]
                    diretores[j], diretores[j + 1] = diretores[j + 1], diretores[j]
                    anoLancamento[j], anoLancamento[j + 1] = anoLancamento[j + 1], anoLancamento[j]
                    generos[j], generos[j + 1] = generos[j + 1], generos[j]

            else:
                print("Opção inexistente.")
                return
    
    print("Filmes ordenados com sucesso.")

# Lista tudo
def listarFilmes():

    if len(titulos) == 0:
        print("Não existem filmes cadastrados no catálogo.")
        return
    
    for i in range(len(titulos)):
        print(f"Posição: {i}\ntitulo: {titulos[i]} diretor: {diretores[i]} ano: {anoLancamento[i]} género: {generos[i]}\n---------Outro Filme---------")

# Menu
def menu():
    while True:
        print("\n1 - Adicionar novo filme")
        print("2 - Procurar por título, diretor ou género")
        print("3 - Excluir filme")
        print("4 - Ordenar filmes")
        print("5 - Listar filmes")
        print("6 - Sair do Programa")

        opc = int(input("Escolhe a opção com o número associado.\n"))

        if opc == 1:
            cadastrarFilme()    
        elif opc == 2:
            procurarFilmes()
        elif opc == 3:
            excluirFilme()
        elif opc == 4:
            ordenarFilmes()
        elif opc == 5:
            listarFilmes()
        elif opc == 6:
            print("A sair do Programa!")
            break
        else:
            print("Número não existe.")
menu()