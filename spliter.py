def spliting(main,many):
    splitinglist=[]
    for splitingmany in range(0,many):
        splitinglist.append(int(main.split(" ")[splitingmany]))
    return splitinglist


#기존의 스플리팅보다 더 간단하고 더 사용이 쉬움
#spliting 3.2.6 V2
#mainS: 나누고싶은 문자열(    [문자열]" "[문자열]...    )
def spliting(mainS):
    mainS=str(mainS)
    slpitinglist=[]
    slpitinglist=mainS.split(" ")
    return slpitinglist