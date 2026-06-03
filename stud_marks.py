student_marks ={
    "Reena":90,
    "Rohit":78,
    "Sonia":85,
    "Sai":41,
    "Raj":65,
    "priya":55,
    "shiv":35,
    "Ravi":99
}
for i in student_marks:
    if student_marks[i] >= 91:
        print(i,"Grade A+")
    elif student_marks[i] >= 81:
        print(i,"Grade A")
    elif student_marks[i] >= 71:
        print(i,"Grade B+")
    elif student_marks[i] >= 61:
        print(i,"Grade B")
    elif student_marks[i] >= 51:
        print(i,"Grade C")
    elif student_marks[i] >= 41:
        print(i,"Grade D")
    else:
        print(i,"Grade F")