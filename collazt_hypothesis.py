c0 = int(input())
i = 0
while c0!= 1 and c0>0 :
    i+=1
    if c0%2==0:
        c0 = int(c0 / 2)
    else:
        c0 = int(3 * c0 + 1)
    print(c0)
print("steps = ",i)
