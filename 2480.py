abc=input()
a=int(abc.split(" ")[0])
b=int(abc.split(" ")[1])
c=int(abc.split(" ")[2])
if a==b==c:
    money=10000+a*1000
elif a==b:
    money=1000+a*100
elif a==c:
    money=1000+c*100
elif b==c:
    money=1000+b*100
else:
    money=100*(max(a,b,c))
print(money)
