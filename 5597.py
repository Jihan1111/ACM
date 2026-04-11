all_students = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]


for i in range(28):
    student_number = int(input())
    index = student_number - 1
    
    all_students[index] = True

number = 1

for j in all_students:
    if(j == False):
        print(number)

    number = number + 1