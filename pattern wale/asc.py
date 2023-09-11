count=5
for i in range(1,10):
    if(i<=5):
        count-=1
    else:
        count+=1
        print("*",end="")
    print()