def swapv1(exampleswap1,exampleswap2):
    swapv1tmp=exampleswap1
    exampleswap1=exampleswap2
    exampleswap2=swapv1tmp
    return exampleswap1,exampleswap2
def spliting(main,many):
    splitinglist=[]
    for splitingmany in range(0,many):
        splitinglist.append(int(main.split(" ")[splitingmany]))
    return splitinglist

nm=input()
l=[]
k=0
n,m=spliting(nm,2)

for uiu in range(0,n):
    l.append(uiu+1)

#print(n, " uidgaefjhisdga", m) 
for a in range(0,m):
    ij=input()
    i,j=spliting(ij,2)
    #i,j바꾸기
    #i=1,j=4
    i=i-1
    j=j-1
    for o in range(i,((i+j)//2+1)):
        #print(o,j-o-1)
        l[o],l[i+j-o]=swapv1(l[o],l[i+j-o])
        #l[o],l[j-o]=swapv1(l[o],l[o])
for qwertyuiop in range(0,len(l)):
    print(l[qwertyuiop],end=' ')
    