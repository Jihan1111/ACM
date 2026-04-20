from pickle import LIST


def spliting(mainS):
    mainS=str(mainS)
    slpitinglist=[]
    slpitinglist=mainS.split(" ")
    return slpitinglist

def ring(mom):
    uu=0
    if mom=="A"or mom=="B"or mom=="C":
        uu=2
    elif mom=="D"or mom=="E"or mom=="F":
        uu=3
    elif mom=="G"or mom=="H"or mom=="I":
        uu=4
    elif mom=="J"or mom=="K"or mom=="L":
        uu=5
    elif mom=="M"or mom=="N"or mom=="O":
        uu=6
    elif mom=="P"or mom=="Q"or mom=="R"or mom=="S":
        uu=7
    elif mom=="T"or mom=="U"or mom=="V":
        uu=8
    elif mom=="W"or mom=="X"or mom=="Y"or mom=="Z":
        uu=9
    return uu
    
a=str(input())
b=list(a)
for i in range(0,len(b)):
    b[i]=ring(b[i])
    b[i]=b[i]+1
print(sum(b))