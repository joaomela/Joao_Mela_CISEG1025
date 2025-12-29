def VerNumeros():
    acc = 0
    opc2 = "O"
    flag = True 
    while flag:   
        for t in range(0,100):
            number = int(input("\nEscreve um valor\n"))
            while number < 1 or number > 1000:
                number = int(input("\nEscreve um valor dentro do intervalo de 1-1000\n"))
            divisores = 0
            perfeito = 0
            flagPrimo = True
            flagPar = (number % 2 == 0)
            if number > 1:
                for i in range(2, number):
                    if number % i == 0:
                        flagPrimo = False
                for i in range(1, number+1):
                    if number % i == 0:
                        divisores+=1
                for i in range(1, number):
                    if number % i == 0:
                        perfeito+=i
            elif number == 1:
                flagPrimo = False
                divisores = 1
                perfeito = 0
            if flagPrimo:
                print("O numero e primo")
            else:
                print("O numero nao e primo")
            if flagPar:
                print('O numero e Par')
            else:
                print('O numero e impar')
            if perfeito == number:
                print('Número é perfeito')
            else:
                print('Número nao é perfeito')
            acc+=1
            if acc >= 10:
                while opc2 != "S" and opc2 != "N":

                    opc2 = input("\nQueres ver mais 10 valores?(S/N)\n")
                    if opc2 == "S":
                        acc = 0

                    elif opc2 == "N":
                        break
                
            if opc2 == "N":
                flag = False
                break
            opc2 = "O"
                

            print('Numero de divisores', divisores)

while True:
    print("Menu\n1 - ver números\n2 - Sair do Programa")
    opc = int(input())
    if opc == 1:
        VerNumeros()
    elif opc == 2:
        break
    else:
        continue

library = [
        
    ]

def cadastrarLivro():
    livro_existe = False
    if len(library) < 100:
        titulo = input("Titulo do livro\n")
        autor = input("Autor do livro\n")
        anoDePub = input("Ano de Publicaçao\n")
        for livro in library:
            if (livro['titulo'] == titulo.lower() and livro['autor'] == autor.lower()):
                livro_existe = True
        if not livro_existe:
            library.append({'titulo' : f'{titulo}', 'autor' : f'{autor}', 'ano' : f'{anoDePub}'})
            print(f"\nLivro cadastrado com sucesso!")
            print(f"Título: {titulo}")
            print(f"Autor:  {autor}")
            print(f"Ano:    {anoDePub}")
    else:
        print("Limite máximo atingido de 100 livros")

        

def procurarLivro(metodo):

    if metodo == "autor":
        nome = input("Nome do autor\n")
        for pos, livro in enumerate(library):
                if livro['autor'] == nome.lower():
                    print(f"\nLivro de {nome} encontrado",f"\n{livro}",f"Posição {pos}")
    elif metodo == "titulo":
        titulo = input("escreve o Titulo\n")
        for pos, livro in enumerate(library):
                if livro['titulo'] == titulo.lower(): 
                    print(f"\nLivro de {titulo} encontrado",f"\n{livro}")

def excluirLivro():
    opcExcluir = int(input("Escreve o numero do livro que queres eliminar\n"))
    del library[opcExcluir]

def ordenarLivro(criterio):
    if criterio == "titulo":
        livros_ordenados_titulo = sorted(library, key=lambda x: x['titulo'])
        print(livros_ordenados_titulo)
    elif criterio == "autor":
        livros_ordenados_autor = sorted(library, key=lambda x: x['autor'])
        print(livros_ordenados_autor)

while True:

    print("1 - Adicionar novo Livro\n2 - Procurar por titulo ou autor\n3 - Excluir livro\n4 - Ordenar Livros\n5 - Listar livros\n6 - Sair do Programa")
    opc = int(input("\nEscreve a opçao\n"))

    if opc == 1:

        cadastrarLivro()

    elif opc == 2:

        metodo = input("Queres procurar por autor ou titulo\n")
        procurarLivro(metodo)

    elif opc == 3:

        excluirLivro()

    elif opc == 4:

        criterio = input("Queres ordenar por titulo ou autor\n")
        ordenarLivro(criterio)

    elif opc == 5:

        print(library)

    elif opc == 6:

        break

    else:

        continue
