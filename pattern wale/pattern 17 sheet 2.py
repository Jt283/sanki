for i in range(1,6):
    if (i<=2):
        for j in range(0,i):
            print("*",end="")
    elif(i<=6 ):
        print("*",end="")
    
    if(i>2 and i<5):
        for y in range(2,i):
            print(" ",end="")
    
    if(i>2 and i<5):
        print("*",end="")
    elif(i>=5):
        for l in range (i,9):
            print("*",end="")

    print()