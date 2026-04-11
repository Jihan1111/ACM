def spliting(main,many):
    splitinglist=[]
    for splitingmany in range(0,many):
        splitinglist.append(int(main.split(" ")[splitingmany]))
    return splitinglist
def swapv1(exampleswap1,exampleswap2):
    swapv1tmp=exampleswap1
    exampleswap1=exampleswap2
    exampleswap2=swapv1tmp
    return str(exampleswap1),str(exampleswap2)

ab=str(input())
a,b=spliting(ab,2)
al,bl=[""],[""]
al,bl=list(str(a)),list(str(b))
# print(al)
# print(bl)
al[0],al[2]=swapv1(al[0],al[2])
bl[0],bl[2]=swapv1(bl[0],bl[2])
print(al)
print(bl)
a=al[0]+al[1]+al[2]
b=bl[0]+bl[1]+bl[2]
a,b=int(a),int(b)
if a>b:
    print(str(a))
else:
    print(str(b))