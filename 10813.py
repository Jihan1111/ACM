def spliting(main,many):
    splitinglist=[]
    for splitingmany in range(0,many):
        splitinglist.append(int(main.split(" ")[splitingmany]))
    return splitinglist

nm=input()
n,m=spliting(nm,2)
l=[]
tmp=0
for p in range(0,n):
    l.append(p+1)
for o in range(0,m):
    ij=input()
    i,j=spliting(ij,2)
    i,j=i-1,j-1
    tmp=l[i]
    l[i]=l[j]
    l[j]=tmp
for t in range(0,n):
    print(l[t],end=" ")
