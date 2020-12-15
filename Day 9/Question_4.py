grade = int(input("Enter the grade: "))

if(grade >= 80 and grade <= 100):
    print("A")
elif(grade >= 70 and grade <= 79):
    print("B")
elif(grade >= 60 and grade <= 69):
    print("C")
elif(grade >= 50 and grade <= 59):
    print("D")
elif(grade >= 0 and grade <= 49):
    print("F")