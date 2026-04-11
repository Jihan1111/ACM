def spliting(main,many):
    splitinglist=[]
    for splitingmany in range(0,many):
        splitinglist.append(int(main.split(" ")[splitingmany]))
    return splitinglist
#------------------:-0

n=int(input())
g=input()
gwamok=[]
gwamok.append(spliting(g,n))
m=max(gwamok)
for i in range(0,n):
    gwamok[i]=gwamok[i]/m*100