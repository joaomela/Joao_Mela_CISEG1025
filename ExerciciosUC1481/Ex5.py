import re

arquivo = open("C:/Users/Joao/Desktop/dados.json", "r")

conteudo = arquivo.read()

print(conteudo)

padrao_email = r"[a-zA-Z0-9._%+-]+@[a-z-.]+\.[a-z]+"

emails = re.findall(padrao_email, conteudo)

for email in emails:
    print(email)

padrao_dominio = r"https?://([a-zA-Z-]+\.[a-z]+)"

dominios = re.findall(padrao_dominio, conteudo)

for dominio in dominios:
    print(dominio)

padrao_nif = r"[123568][0-9]{8}"

nifs = re.findall(padrao_nif, conteudo)

for nif in nifs:
    print(nif)

padrao_tele = r"[9][0-9]{8}"

teles = re.findall(padrao_tele, conteudo)

for tele in teles:
    print(tele)

with open("C:/Users/Joao/Desktop/novosdados.json", "w") as f:
    for email, nif, telemovel in zip(emails, nifs, teles):
        f.write(f"{email} | {nif} | {tele}\n")

dados = [
    {"nome": "Ana Costa", "email": "ana.costa@gmail.com"},
    {"nome": "Joao Silva", "email": "joao_silva@empresa.com"},
]

with open("C:/Users/Joao/Desktop/novosdados3.txt", "w") as arquivo:
    for pessoa in dados:
        arquivo.write(f"nome: {pessoa['nome']}, email: {pessoa['email']}\n")
