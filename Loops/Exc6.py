
gP = 0 
for i in range(1,100):
    nP = 0
    for n in range(1,i+1):
        if i % n == 0:
            nP+=1
    if nP == 2:
        print(i)
        gP+=1
    if gP==10:
        break
