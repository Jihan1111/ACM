x=int(input())
n=int(input())
for i in range(n+1):
    a,b=int(input()).split(" ")
    o=a*b
if x==o:
    print("yes")
else:
    print("no")
    