a=int(input("Enter number: "))
b=[i for i in range(2,100) if a%i==0]
print(b)
c=min(b)
print(c)