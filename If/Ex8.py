notas = []

for i in range(10):
    nota = float(input(f"Escreve uma nota do aluno {i+1} (de 0 a 20): "))
    notas.append(nota)

media = sum(notas) / len(notas)
acima = 0
for nota in notas:
    if nota >= media:
        acima += 1
    
print("Média:",media,"Acima da média:",acima)