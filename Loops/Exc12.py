n=int(input("n"))
acc=0
for i in range(1,n):
    print(f"{n} + {i} = {n+i}")
    print(f"{n} - {i} = {n-i}")
    print(f"{n} * {i} = {n*i}")
    print(f"{n} / {i} = {n/i}")
    acc+=4
print(acc)