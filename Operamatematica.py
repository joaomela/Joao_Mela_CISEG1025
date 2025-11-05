v1 = int(input("escreve numero"))
v2 = int(input("escreve numero"))
operação = input("operaçao")

if operação == "+":
    print(v1+v2)
elif operação == "-":
    print(v1-v2)
elif operação == "*":
    print(v1*v2)
elif operação == "/":
    print(v1/v2)
elif operação == "//":
    print(v1//v2)
elif operação == "**":
    print(v1**v2)
else: 
    print("tenta outra vez")