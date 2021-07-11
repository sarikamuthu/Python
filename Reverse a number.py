a=int(input("Enter a number: "))
rev=0
temp=a
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
print("The reverse of a number is:",rev)