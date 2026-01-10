n=int(input())
al=input()
l=[]
a=0
b=0
num=None
for base in range(0,n):
    l.append(int(al.split(" ")[base]))
#print(l)
anum=min(l)
bnum=max(l)
# for chack in range(0,n):
#     if l[chack]<l[anum]:
#         anum=l[chack]
#     elif l[chack]>l[bnum]:
#         bnum=l[chack]
#     else:
#         pass
print(anum,bnum)