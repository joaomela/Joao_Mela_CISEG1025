nomes = [ 

    "Pedro Pereira", 

    "Ana Beatriz", 

    "Ana Clara", 

    "Carlos Silva", 

    "Beatriz Souza", 

    "Ana Paula", 

    "Pedro Andrade" 

] 
print(nomes)

def ordena_nomes_ascii_quicksort(lista):
    
    if len(lista) <= 1:
        return lista
    
    pivot = lista[0]

    menores = [x for x in lista[1:] if x <= pivot]
    maiores = [x for x in lista[1:] if x > pivot]

    return ordena_nomes_ascii_quicksort(menores) + [pivot] + ordena_nomes_ascii_quicksort(maiores)


nomes = ordena_nomes_ascii_quicksort(nomes)
print(nomes)