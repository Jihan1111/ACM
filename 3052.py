NUMBER = 42

l=[]
q=[]

for inputi in range(0,10):
    a=int(input())
    l.append(a)
    a=None
for i in range(0,10):
    n = l[i]%NUMBER

    if (n in q):
        pass
    else:
        q.append(n)
a=len(q)
print(a)
