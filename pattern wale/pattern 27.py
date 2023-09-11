count=6
for i in range(1,10):
    if(i<=5):
        count-=1
        for j in range(0,count):
            print(" ",end="")
    else:
        count+=1
        for k in range(0,count):
            print(" ", end="")
    if(i>=0):
        print("*",end="")
    if(i>1 and i<=5):
        r=2*(i-1)-1
        for l in range(0,r):
            print(" ",end="")
    elif(i>5):
        y=7-2*(i-5)
        for m in range(0,y):
            print(" ",end="")
    if(i>=2 and i<9):
        print("*",end="")
    print()