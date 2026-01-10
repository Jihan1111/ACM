ppap=input()
n=int(ppap.split(" ")[0])
x=int(ppap.split(" ")[1])
lnum=input()
num=0
l=[]
al=[]
for start_base in range(0,n):
    num=int(lnum.split(" ")[start_base])
    l.append(num)
    num=None
    #print(l)
#print(l)
a=0
for chacking in range(0,n):
    if l[chacking]<x:
        a=a+1
        al.append(l[chacking])
for o in range(0,a):
    print(al[o],end=' ')