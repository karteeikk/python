num_student=int(input("enter the number of student : "))
for i in range(num_student):
    print(f"\nstudent{i+1} : ")
    total=0
    mark=[]
    for j in range(3):
        sub_marks=int(input(f"subject marks {j+1} "))
        mark.append(sub_marks)
        total+=sub_marks
        per=(total/300)*100
        if per > 70:
            grade = "DIST"
        elif per > 60:
            grade = "FIRST"
        elif per > 50:
            grade = "SECOND"
        elif per > 40:
            grade = "PASS"
        else:
            grade = "FAIL"
    print(f"total marks : {total}")
    print(f"per : {per:.2f}%")
    print(f"grade : {grade}")

