count=0
count1=0
for i in range(1,10):
    if(i>1 and i<=5):

        count+=1
        for j in range(0,count):
            print(" ",end="")
    elif(i>5):
        count-=1
        for k in range(0,count):
            print(" ",end="")
    if(i>0):
        print("*",end="")
    if(i==1):
        n=9*i
        for l in range(0,n):
            print("*",end="")
    if(i>1 and i<=5):
        u=8-2*(i-1)
        for m in range(0,u):
            print(" ",end="")
    elif(i>=6 and i<9):
        s=2*(i-5)
        for n in range(0,s):
            print(" ",end="")
    if(i==9):
        w=8*(i-8)
        for o in range(0,w):
            print("*",end="")
    if(i>1 and i!=5):
        print("*",end="")
    print()

