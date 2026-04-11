#spliting(분해되는 변수)
def spliting(mainS):
    mainS=str(mainS)
    slpitinglist=[]
    slpitinglist=mainS.split(" ")
    return slpitinglist

c=int(input())
save=[]
for i in range(0,c):
    teacher=input()
    many,alpa=spliting(teacher)
    alpa=str(alpa)
    alpas=list(alpa)
    saveint=""
    for j in range(0,len(alpas)):
        tmp=""
        for o in range(0,int(many)):
            tmp=tmp+alpas[j]
        saveint=saveint+tmp
    save.append(saveint)
#save정상작동 확인됨: 'aaabbbccc'
for hh in range(0,len(save)):
    print(save[hh])
    