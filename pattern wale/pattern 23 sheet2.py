count=6
count1=0
for i in range(1,10):
    if(i<=5):
        count-=1
        for j in range(1,count):
            print(" ",end="")
    elif(i>5 ):
        count+=1
        for k in range(1,count):
            print(" ",end="")
    
        
    if(i<=2):
        for l in range(0,i):
            print("*",end="")
    elif(i>2 and i<=8):
        print("*",end="")
    elif(i>=8 and i<10):
        for p in range(i,10):
            print("*",end="")
    if(i>=3 and i<=5):
        count1+=1
        for q in range(0,count1):
            print(" ",end="")
    elif(i>=6 and i<=8):
        count1-=1
        for y in range(count1,0,-1):
            print(" ",end="")
    if(i>2 and i<9):
        print("*",end="")
    
    print()

