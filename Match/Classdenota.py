"""2. Classificação de nota 

Lê uma nota (0–100) e retorna uma classificação: 

90 ou mais → Excelente 

70–89 → Bom 

50–69 → Suficiente 

Abaixo de 50 → Insuficiente 

Exemplo: 
Entrada → 72 
Saída → Bom """


nota = int(input("escreve nota de 0-100!"))

if nota >= 90 and nota < 101:
    print("Excelente")
elif nota >= 70 and nota < 90:
    print("Bom")
elif nota >= 50 and nota < 70:
    print("Suficiente")
elif nota < 50 and nota > -1:
    print("Insuficiente")
else: print("Engano")