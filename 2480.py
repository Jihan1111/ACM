a,b,c=raw_input().split(" ")
a=int(a)
b=int(b)
c=int(c)

if a==b==c:
    money=10000+a*1000
elif a==b or b==c or a==b:
    money=1000+a*100
else:
    money=max(a,b,c)
print(money)
#eS,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,