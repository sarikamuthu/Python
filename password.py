for i in range(0,3):
    n=input("Enter the password: ")
    if n=="PyThOn":
        print("Hi!Welcome to python")
        break
    else:
        if i==1 or i==0:
            print("Wrong attempt,you have",2-i,"more chances")
        else:
            print('Invalid login')