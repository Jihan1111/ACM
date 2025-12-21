t=int(input())
l=[]
al=[]
bl=[]
for i in range(1,t+1):
    ab=input()
    a=int(ab.split(" ")[0])
    al.append(a)
    b=int(ab.split(" ")[1])
    bl.append(b)
    c=a+b
    l.append(c)
for h in range(1,t+1):
    print("Case ","#",h,": ",al[h-1]," + ",bl[h-1]," = ",l[h-1],sep='')