mark_list=[90, 85, 78, 98, 67]

for i in range(5):
    a=int(input("Enter marks:"))
    mark_list.append(a)
print(mark_list)
def assign_grade(mark_list):
    grade_list=[]
    for i in mark_list:
        if i>=90:
            grade_list.append("A")
        if i>=80 and i<90:
            grade_list.append("B")
        if i>=65 and i<80:
            grade_list.append("C")
        if i>=40 and i<=65:
            grade_list.append("D")
        if i<40:
            grade_list.append("F")
    return (grade_list)
print(assign_grade([90, 69, 85, 98, 12]))

q=zip(mark_list,assign_grade(mark_list))
print(list(q))