def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i,j,k=0,0,0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i=i+1
                
            else:
                list1[k]=right_list[j]
                j=j+1
            k+=1   
        while i<len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            list1[k]=right_list[j]
            j+=1
            k+=1
    print(list1)

n=int(input("Enter number of elements: "))
a=[int(input("Enter element:")) for i in range(n)]
print(mergesort(a))