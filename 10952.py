s=0
l=[]
count=0
while s==0:
    count=count+1
    xy=input()
    x=int(xy.split(" ")[0])
    y=int(xy.split(" ")[1])
    if x == 0 and y == 0:
        s=1
    else:
        c=x+y
        l.append(c)
for i in range(0,count-1):
    print(l[i])