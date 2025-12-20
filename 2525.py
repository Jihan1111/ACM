hm=input()
h=int(hm.split(" ")[0])
m=int(hm.split(" ")[1])
t=int(input())
m=m+t
while m>=60:
    if m>=60:
        m=-1*(60-m)
        h=h+1
        if h>=24:
            h=-1*(24-h)
print(h,m)
