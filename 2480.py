a,b,c=input().split()
h=int(h)
m=int(m)
m=m-45

if m<0:
    m=60+m
    h=h-1
    if h<0:
        h=24+h

print(h,m)

