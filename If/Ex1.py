secs = int(input("Escreve os segundos para converter"));

segundos = int(secs % 60);
minutos = int((secs % 3600) / 60);
horas = int(secs / 3600);

print(horas,minutos,segundos, sep=":");