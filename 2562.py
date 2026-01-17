l=[]
for i in range(0,9):
    nine=input()
    l.append(nine)
    nine=None
a=False
b=0
while a==False:
    if l[b]==max(l):
        a=True
    b=b+1
print(max(l))
print(b)