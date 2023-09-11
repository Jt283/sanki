count=0
count1=3
for i in range(1,10):
    if(i==1):
        n=5*i
        for j in range(0,n):
            print("*",end="")
    elif(i==9):
        k=5*(i-8)
        for l in range(0,k):
            print("*",end="")
    if(i>1 and i<=5):
        count+=1
        for k in range(0,count):
            print(" ",end="") 
    elif(i>5 and i<=9):
        count-=1
        for t in range(0,count):
            print(" ",end="")
    if(i>1 ):
        print("*",end="")
    if(i>1 and i<=5) :
        count1-=1
        for w in range(0,count1):
            print(" ",end="")
    if(i>5 and i<=8):
        count1+=1
        for x in range(0,count1):
            print(" ",end="")
    if(i>=2 and i!=5 and i<=8):
        print("*",end="")
    print()

