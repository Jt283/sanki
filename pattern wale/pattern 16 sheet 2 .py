count=6
count1=6
for i in range(1,11):
    if(i<=5):
        count-=1
        for k in range(0,count):
            print("*",end="")
    else:
        count+=1
        for j in range(1,count):
            print("*",end="")
    if(i<=5):
        n=2*(i-1)
        for l in range(0,n):
            print(" ",end="")
    else:
        k=10-2*(i-5)
        for t in range(0,k):
            print(" ",end="")
    if(i<=5):
        count1-=1
        for q in range(0,count1):
            print("*",end="")
    else:
        count1+=1
        for e in range(1,count1):
            print("*",end="")

    print()
   