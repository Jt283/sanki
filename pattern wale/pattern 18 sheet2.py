for i in range(1,6):
    if(i==1):
        for i in range(1,i+5):
            print("*",end="")
    elif(i>1 and i<4):
        print("*", end="")
    elif(i>=4):
        for d in range (i,6):
            print("*",end="")
    if(i>1 and i<4):
        for t in range(i,4):
            print(" ",end="")
    if(i>1 and i<4):
        print("*", end="")
    print()
    