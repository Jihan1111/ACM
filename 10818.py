n=int(input())
al=input()
l=[]
a=0
b=0
num=None
for base in range(0,n):
    l.append(int(al.split(" ")[base]))
anum=min(l)
bnum=max(l)
print(anum,bnum)