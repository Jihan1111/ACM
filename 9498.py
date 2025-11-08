grade = input()
grade = int(grade)

if grade in range (90, 101):
    print("A")

elif grade in range (80, 89):
    print("B")

elif grade in range (70, 79):
    print("C")

elif grade in range (60, 69):
    print("D")

else:
    print("F")
