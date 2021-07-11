students={}
n=int(input("Enter number of students: "))
for i in range(n):
    sname=input("Enter name:")
    marks=[]
    for j in range(5):
        mark=int(input("Enter mark:"))
        marks.append(mark)
    students[sname]=marks
