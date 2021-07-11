def quicksort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()
    items_greater=[]
    items_smaller=[]
    for items in sequence:
        if items<pivot:
            items_greater.append(items)
        else:
            items_smaller.append(items)
    return quicksort(items_greater)+[pivot]+quicksort(items_smaller)
print(quicksort([7,2,9,1,5,6,99]))