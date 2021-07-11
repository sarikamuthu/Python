def selectionsort(a):
    for i in range(0,len(a)):
        for j in range(len(a)-1,i,-1):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a

f=open("numbers.txt",'r',errors="ignore") 
m=f.read()
b=list(map(int, m.split(',')))
print(selectionsort(b))