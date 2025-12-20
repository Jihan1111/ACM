q=int(input())
l=[]
for i in range(0,q):
    ab=input()
    a=int(ab.split(" ")[0])
    b=int(ab.split(" ")[1])
    c=a+b
    l.append(c)
for o in range(0,q):
    print(l[o])
#완료