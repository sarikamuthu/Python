def add(a,b):
    c=[[0 for j in range(len(a[0]))]for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j]=a[i][j]+b[i][j]
    return c
def subtract(a,b):
    c=[[0 for j in range(len(a[0]))]for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j]=a[i][j]-b[i][j]
    return c
def multiply(a,b):
    m=len(a)
    n=len(a[0])
    q=len(b[0])
    c=[[0 for j in range(len(a[0]))]for i in range(len(a))]
    for i in range(m):
        for j in range(n):
            for k in range(q):
                c[i][j]+=a[i][k]*b[k][j]
    return c
m=int(input('Enter rows of first matrix'))
n=int(input("Enter column for first matrix"))
p=int(input('Enter rows of second matrix'))
q=int(input("Enter column for second matrix"))
a=[[int(input("Enter: "))for j in range(n)]for i in range(m)]
b=[[int(input("Enter: "))for j in range(q)]for i in range(p)]
print("1.Add  2.Subtract 3.Multiply")
ch=int(input('Enter choice number: '))
if ch==1:
    print(add(a,b))
elif ch==2:
    print(subtract(a,b))
elif ch==3:
    print(multiply(a,b))
else:
    print("INVALID")