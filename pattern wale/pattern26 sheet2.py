for i in range(1,6):
    for j in range(0,i-1):
        print(" ",end="")
    if(i>=1):
        print("*",end="")
    if(i>1):
        u=7-2*(i-1)
        for k in range(0,u):
            print(" ",end="")
    if(i==1):
        n=i*7
        for y in range(0,n):
            print("*",end="")
    if(i>=1 and i<5):
        print("*",end="")
    print()