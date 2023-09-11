for i in range(1,10):
    if(i==1):
        n=5*i
        for j in range(0,n):
            print("*",end="")
    if(i>1 and i<9):
        print("*",end="")
    if(i==9):
        m=5*(i-8)
        for k in range(0,m):
            print("*",end="")
    if(i>=2 and i<=3):
        for l in range(i,4):
            print(" ",end="")
    if(i>=2 and i<=4):
        print("*",end="")
    if(i>=7 and i<=8):
        for r in range(6,i):
            print(" ",end="")
    if(i>=6 and i<=8):
        print("*",end="")
    print()