a = int(input("numero"))
nD=0
for i in range(1,a+1):
    if a % i == 0:
        nD+=1

print(nD)