count=0
count1=0
for i in range(1,10):
    if(i<=5):
        count+=1
        for j in range(0,count):
            print("*",end="")
    else:

        count-=1
        for k in range(count,0,-1):
            print("*",end="")
    if(i<=5):
        k=10-2*i
        for g in range(k,0,-1):
            print(" ",end="")
    else:
        o=2*(i-5)
        for r in range(0,o):
            print(" ",end="")
    if(i<=5):
        count1+=1
        for v in range(0,count1):
            print("*",end="")
    else:
        count1-=1
        for t in range(count1,0,-1):
            print("*",end="")
    print()