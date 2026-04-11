#1152에서 문자열은 지워지지 않는다는 사실을 깨달고, 숫자로 바꿔서 지우는 형식의 함수를 만듬

#----------------------------------------------------listdel 1.0.4-v1
#문자열 형태의 리스트를 입력받고,지우고 싶은 문자도 입력받아서 리스트를 아스키코드의 형태(int)로 전환 후, 해당 문자가 포함된 모든 인덱스를 지우고 다시 문자열로 바꾸는 프로그램
#사용법 list=listdel(지우고 싶은 문자,문자열 형태의 리스트)
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

#----------------------------------------------------