count=0
for i in range(1,11):
    if(i<=6):
        count+=1
     
    else:
        count-=1
    for j in range(1,count):
        print("*",end="")
    print()