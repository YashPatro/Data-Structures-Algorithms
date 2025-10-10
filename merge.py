#10/10/25

list1 = [9,3,7,5,6,4,1]
def mergeSort(l):
    if len(l) <= 1:
        return l
    m = len(l)//2
    left = l[0:m]
    print(left)
    right = l[m:]
    l1 = mergeSort(left)
    l2 = mergeSort(right)
    return merge(l1,l2)
def merge(l1,l2):#a = left list, b= right list
    i = j = 0
    outputL = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            outputL.append(l1[i])
            i+=1
        else:
            outputL.append(l2[j])
            j+=1
    print(outputL)

data = mergeSort(list1)
print(data)