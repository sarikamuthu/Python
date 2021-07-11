d={
    "parisa":"22/9/2002",
    "suvarna":"6/8/2002",
    "priya":"18/2/2003"
}
a=input('Enter name: ')
# b=input("Enter dob: ")
if a in d:
    print("Present")
else:
    b=input("Enter dob: ")
    if b in d.values():
        print("DOB present")
    else:
        # a=input('Enter name: ')
        # b=input("Enter dob: ")
        print("Updated")
        d.update({a:b})
        print("Updated")
print(d)