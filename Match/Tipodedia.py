#*1. Tipo de dia 

#Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana. 

#Exemplo: 
#Entrada → domingo 
#Saída → Fim de semana

dia = input("Introd o dia da semana!")

if "feira" in dia:
    print("Dia útil")
else: print("Fim de semana")