count=0
count1=11
for i in range(1,10):
    if(i<=5):
        count+=1
    else:
        count-=1
    for j in range(1,count):
        print(" ",end="")
    
    if(i<=5):
        count1-=2
    else:
        count1+=2
    for k in range(0,count1):
        print("*",end="")

    print()