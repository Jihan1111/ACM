t=int(input())
l=[]
for i in range(1,t+1):
    ab=input()
    a=int(ab.split(" ")[0])
    b=int(ab.split(" ")[1])
    c=a+b
    l.append(c)
for h in range(1,t+1):
    print("Case ","#",h,": ", l[h-1],sep='')