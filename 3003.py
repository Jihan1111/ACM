def spliting(mainS):
    mainS=str(mainS)
    slpitinglist=[]
    slpitinglist=mainS.split(" ")
    return slpitinglist

n=spliting(input())
t=[1, 1, 2, 2, 2, 8]
for u in range(0,6):
    n[u] = int(n[u])
for i in range(0,6):
    f = t[i]-n[i]
    print(f, end=' ')