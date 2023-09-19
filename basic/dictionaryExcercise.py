student_score = {"Anis": 81, "Sibber": 78, "Jahid": 99, "Gopal": 74, "Odity": 62}

student_grade = {}

for num in student_score:
    if student_score[num] > 90 and student_score[num] <= 100:
        student_grade[num] = "Outstanding"
    elif student_score[num] > 80 and student_score[num] <= 90:
        student_grade[num] = "Exceeds"
    elif student_score[num] > 70 and student_score[num] <= 80:
        student_grade[num] = "Acceptable"
    elif student_score[num] <= 70:
        student_grade[num] = "Fail"

print(student_grade)
