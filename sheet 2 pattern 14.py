count=0
for i in range (1,6):
    for j in range(i,6):
        print("*",end="")
    count+=2
    for k in range(2,count):
        print(" ",end="")
    for j in range(i,6):
        print("*",end="")
   
    
    print()