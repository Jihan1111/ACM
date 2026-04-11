def lol(target, lisst, length):
    result = -1 
    for sd in range(0, length):
        if lisst[sd] == target: 
            result = sd
            break 
    return result
a=input()
al=list(a)
long=len(al)
l=[]
#---------------------------------------------------------]
alpa=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","x"]
for i in range(0,len(alpa)):
    l.append(lol(alpa[i],al,long))
#-------[낄낄]---------------------------------------------]
for h in range(0,len(l)):
    print(l[h]," ",end="")
