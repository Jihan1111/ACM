x=int(input())
n=int(input())
for i in range(n+1):
    a,b=int(input()).split(" ")
    o=a*b
    l=[]
    l.append(o)
lk=sum(l)
if x==lk:
    print("yes")
else:
    print("no")
    