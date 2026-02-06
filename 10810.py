#def test(main,many):

def spliting(main,many):
    splitinglist=[]
    for splitingmany in range(0,many):
        splitinglist.append(int(main.split(" ")[splitingmany]))
    return splitinglist

nm=input()
n,m=spliting(nm,2)
bowl=[]
for bowlpusher in range(0,n):
    bowl.append(0)
for p in range(0,m):
    ijk=input()
    i,j,k=spliting(ijk,3)
    for o in range(0,(j+1)-i):
        bowl[o+(i-1)]=k
for s in range(0,n):
    print(bowl[s],end=(" "))
