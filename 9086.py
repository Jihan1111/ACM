t=int(input())
shell=[]
first=[]
last=[]
for case in range(0,t):
    text=input()
    shell=list(text)

    # 
    last_index = len(text) - 1
    

    first.append(text[0])
    last.append(text[last_index])



    # print(shell)
    # print(max(shell))
    shell=[]
for printg in range(0,t):
    print(first[printg] + "" + last[printg]) # "AC"