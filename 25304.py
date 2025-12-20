x=int(input())
n=int(input())
c=0
for i in range(1,n+1):
    ab=input()
    a=int(ab.split(" ")[0])
    b=int(ab.split(" ")[1])
    c=c+(a*b)
if c==x:
    print("Yes")
elif c!=x:
    print("No")
else:
    pass
