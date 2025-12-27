n=int(input())
p=0
for i in range(1,n+1):
    p=p+1
    for l in range(1,i+1):
        print(" ", end='')
    for t in range(1,p):
        print("*",end='')

    print("\n")