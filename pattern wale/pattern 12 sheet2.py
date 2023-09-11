count=0
cou=10
for i in range(1,11):
    if(i<=5):
        count+=1
     
    else:
        count-=1
    for j in range(2,count):
        print(j,end="")
    print()