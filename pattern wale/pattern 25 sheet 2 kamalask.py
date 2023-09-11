for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    if i>0:

        print("*",end="")
    if(i>1):
        m=(2*(i-1))-1
        for i in range(0,m):
            print(" ",end="")
    if(i>1):
        print("*",end="")
    print()