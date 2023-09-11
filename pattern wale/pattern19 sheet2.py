for i in range(1,6):
    for j in range(i,5):
        print(" ",end="")
    if(i<=2):
        for k in range(0,i):
            print("*",end="")
    elif(i>2 and i<=4):
        print("*",end="")
    elif(i>4):
        for i in range(i,10):
            print("*",end="")
    if(i>2 and i<=4):
        for r in range(2,i):
            print(" ",end="")
    if(i>2 and i<=4):
        
            print("*",end="")
    
    

    print()
