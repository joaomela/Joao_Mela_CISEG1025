import re
import datetime

arquivo = open("C:\\Users\\Joao\\Desktop\\dados.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()

padrao_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(padrao_email, conteudo)


for email in emails:
    print(email)

padrao_telemovel = r"[92](?:[\s-]*\d){8}"

nTelemovel = re.findall(padrao_telemovel, conteudo)


for numero in nTelemovel:
    print(numero)

padrao_nomes = r"(?<=Nome:\s).*?(?=,)"

nomes = re.findall(padrao_nomes, conteudo)


for nome in nomes:
    print(nome)

with open("C:\\Users\\Joao\\Desktop\\extrair.txt", "w", encoding="utf-8") as f:
    for nome, tele, email in zip(nomes, nTelemovel, emails):
        f.write(f"{nome} | {email} | {tele}\n")

padrao_emailpt = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.pt\b"

emailspt = re.findall(padrao_emailpt, conteudo)


for emailpt in emailspt:
    print(emailpt)

arquivo2 = open("C:\\Users\\Joao\\Desktop\\registos.txt", "r")

conteudo2 = arquivo2.read()

print(conteudo2)

arquivo2.close()

padrao_nif = r"[0-9]{9}"

nifs = re.findall(padrao_nif, conteudo2)

for nif in nifs:
    print(nif)

padrao_data = r"[0-3][0-9]/[0-1][0-9]/[0-2][0-9][0-9][0-9]"

datas = re.findall(padrao_data, conteudo2)

for data in datas:
    print(data)

padrao_codigopostal = r"\b\d{4}-\d{3}\b"

codigos = re.findall(padrao_codigopostal, conteudo2)

for codigo in codigos:
    print(codigo)

padrao_site = r"https?://[a-zA-Z-]+\.[a-zA-Z-]{2,}"

sites = re.findall(padrao_site, conteudo2)

for site in sites:
    print(site)

padrao_nifvalido = r"[123568][0-9]{8}"

nifsvalidos = re.findall(padrao_nifvalido, conteudo2)

for nifvalido in nifsvalidos:
    print(nifvalido)

padrao_nomes2 = r"(?<=Nome:\s).*?(?=\|)"

nomes2 = re.findall(padrao_nomes2, conteudo2)

for nome in nomes2:
    print(nome)

with open("C:\\Users\\Joao\\Desktop\\resumo.txt", "w", encoding="utf-8") as f:
    for nome, nif, data, codigo, site in zip(nomes2, nifs, datas, codigos, sites):
        f.write(f"{nome} | {nif} | {data} | {codigo} | {site}\n")

referencia = datetime.datetime(2025, 1, 1)
for data in datas:
    dt = datetime.datetime.strptime(data, "%d/%m/%Y")
    if dt < referencia:
        print(dt.strftime("%d/%m/%Y"))