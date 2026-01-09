listaAluno = []
listaTurma = []

def registarNovo():
    
    while len(listaAluno) >= 100 and len(listaTurma) >= 100:
        print("As listas estão cheias!")
        return

    nome = input("Escreve o nome do Aluno a registar!")
    while nome.split() == "":
       nome = input("Escreve o nome do Aluno a registar!")
    turma = input("Escreve a turma do Aluno a registar!(1.ºA, 2.ºB, 3.ºC)")
    while turma != "1.ºA" and turma != "2.ºB" and turma != "3.ºC":
        turma = input("Escreve a turma do Aluno a registar!(1.ºA, 2.ºB, 3.ºC)")

    for i in range(0,len(listaAluno)):
        if nome == listaAluno[i] and turma == listaTurma[i]:
            print("Esse Aluno já está registado na lista!",listaAluno[i],listaTurma[i])
            return
    listaAluno.append(nome)
    listaTurma.append(turma)

def pesquisarAluno():
    opc = input("Queres pesquisar por turma ou por nome!\n")
    if opc == "turma":
        opc = input("Qual a turma?")
        for i in range(0,len(listaAluno)):
            if  opc == listaTurma[i]:
                print("Registo encontrado",listaAluno[i],listaTurma[i],"\nPosição:",i)
    
    
    elif opc == "nome":
        opc = input("Qual o nome\n")
        for i in range(0,len(listaAluno)):
            if  opc == listaAluno[i]:
                print("Registo encontrado",listaAluno[i],listaTurma[i],"\nPosição:",i)

def eliminarAluno():
    try:
        opc = int(input("Qual a posição que queres eliminar?\n"))
        del listaAluno[opc]
        del listaTurma[opc]
    except ValueError:
        print("Erro de valor")

def ordenarAluno():
    copia = listaAluno.copy()
    copia.sort()
    print(copia)

def listarTudo():
    for i in range(0,len(listaAluno)):
        print(listaAluno[i],listaTurma[i])

while True:
    
    print("1 - Registar novo aluno\n2 - Pesquisar alunos por nome ou turma\n3 - Eliminar aluno por posição\n4 - Ordenar por aluno de A-Z\n5 - Listar Alunos e turmas que cada aluno pertence\n6 - Sair do programa")
    opc = int(input("Opção\n"))

    if opc == 1:
        registarNovo()
    elif opc == 2:
        pesquisarAluno()
    elif opc == 3:
        eliminarAluno()
    elif opc == 4:
        ordenarAluno()
    elif opc == 5:
        listarTudo()
    elif opc == 6:
        break 
