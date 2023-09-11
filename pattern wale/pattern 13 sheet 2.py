for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    n=10-2*i
    for k in range(n,0,-1):
        print(" ",end="")
    for g in range(1,i+1):
        print("*",end="")
    print()