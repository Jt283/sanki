
count=6 
count1=0
for i in range(1,10):
    if(i<=5):
        count-=1
    else:
        count+=1

    for j in range(count,1,-1):
        print(" ",end="")
    
    

    if(i<=5):
        count1+=1
    else:
        count1-=1
    for l in range(1,count1):
        print("*",end="")
    print()
    


