h,m=input().split()
t=int(input())
h=int(h)
m=int(m)
m=m-t

if m<0:
    m=60+m
    h=h-1
    if h<0:
        h=24+h

print(h,m)

