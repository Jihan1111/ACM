n=int(input())
l=[]
num=0
lnum=input()
intv=int(input())
v=0
for start_base in range(0,n):
    num=int(lnum.split(" ")[start_base])
    l.append(num)
    num=None
    #print(l)
#print(l)
for chacking in range(0,n):
    if l[chacking]==intv:
        v=v+1
print(v)