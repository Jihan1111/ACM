n=int(input())
l=[]
for i in range(0,n):
    ab=input()
    a=int(ab.split(" ")[0])
    b=int(ab.split(" ")[1])
    c=a+b
    l.append(c)
for j in range(0,n):
    print(l[j])