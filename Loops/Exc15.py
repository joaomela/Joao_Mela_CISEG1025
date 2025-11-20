n=0
for i in range(0,256):
    print(f"{i} = {chr(i)}")
    n+=1
    if n == 20:
        n=0
        a = input("Queres continuar?('sim/nao')")
        if a == "nao":
            break