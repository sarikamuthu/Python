
a=str(input('Enter string: '))
b=a.replace(" ","")
print(b)

count=0
for i in b:
    count+=1
print("The number of words in sentence is: ",count)