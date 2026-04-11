def spliting(mainS):
    mainS=str(mainS)
    slpitinglist=[]
    slpitinglist=mainS.split()
    return slpitinglist
def listdel(mainl,listl):
    mainl=ord(mainl)
    for listdelmany in range(0,len(listl)):
        listl[listdelmany]=ord(listl[listdelmany])
    for listdelmany1 in range(0,len(listl)):
        if listl[listdelmany1]==mainl:
            del listl[listdelmany1]
    for listdelmany2 in range(0,len(listl)):
        listl[listdelmany2]=chr(listl[listdelmany2])
    return listl
a=str(input())
l=spliting(a)
print(l)
# for i in range(0,len(l)):7
#     if l[i]==" ":
#         l[i]=listdel(l[i],l[i])
print(len(l))
