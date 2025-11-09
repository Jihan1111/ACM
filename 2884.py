h=int(input())
m=int(input())
m=m-45

if m<0:
    m=60+m
    h=h-1
    if h<0:
        h=24+h
else:
    print(h,m)

print(h,m)


