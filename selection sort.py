n=int(input("Enter number of elements: "))
a=[]
for i in range(n):
    new_element=int(input("Enter number: "))
    a.append(new_element)
print(a)

for i in range(0,len(a)):
    for j in range(len(a)-1,i,-1):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
    print(a)