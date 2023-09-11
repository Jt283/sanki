count=0
for i in range(1,6):
    print("*")
    if(i>2 and i<=4):
        count+=1
        for j in range(0,count):
            print("#",end="")
    print()
