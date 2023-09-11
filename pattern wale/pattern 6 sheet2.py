count=7
for i in range(1,10):
    if (i<=5):
        count-=1
    else:
        count+=1

    for j in range(count,1,-1):
        print("*",end="")

    print()

