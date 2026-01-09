# n=int(input())
# p=0
# for i in range(1,n+1):
#     p=p+1
#     for l in range(1,i+1):
#         print(" ", end='')
#     for t in range(1,p):
#         print("*",end='')
#     print("")
n=int(input())
p=0
a=0
b=0
for i in range(0,n):
    p=p+1
    a=n-p
    b=p
    for c in range(0,a):
        print(" ",end='')
    for v in range(0,b):
        print("*",end='')
    print("")
