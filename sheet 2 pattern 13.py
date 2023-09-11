count=10
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    count-=2
    for k in range(0,count):
       print(" ",end="")
    for l in range(1,i+1):
        print("*",end="")

    print()