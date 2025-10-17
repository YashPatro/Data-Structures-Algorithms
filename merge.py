# #10/10/25

# list1 = [8,9,3,7,5,6,4,1]
# def mergeSort(l):
#     if len(l) <= 1:
#         return l
#     m = len(l)//2
#     left = l[0:m]
#     print(left )
#     right = l[m:]
#     l1 = mergeSort(left)
#     l2 = mergeSort(right)

#     return merge(l1,l2)
# def merge(l1,l2):#a = left list, b= right list
#     i = j = 0
        
#     print(l1,l2)
#     outputL = []
#     while i < len(l1) and j < len(l2):
#         if l1[i] <= l2[j]:
#             outputL.append(l1[i])
#             i+=1
#         else:
#             outputL.append(l2[j])
#             j+=1
#     print(outputL)

# data = mergeSort(list1)
# print(data)


#hw

l = [8, 9, 3, 7, 5, 6, 4, 1]

#make each num its own list
lists = []
for x in l:
    lists.append([x])

#keep merging until one list remains
while len(lists) > 1:
    new_lists = []
    for i in range(0, len(lists), 2):
        if i + 1 < len(lists):
            left = lists[i]
            right = lists[i + 1]

            i1 = i2 = 0
            merged = []

# merge two small lists
            while i1 < len(left) and i2 < len(right):
                if left[i1] <= right[i2]:
                    merged.append(left[i1])
                    i1 += 1
                else:
                    merged.append(right[i2])
                    i2 += 1
#add leftover since there is oddnum
            while i1 < len(left):
                merged.append(left[i1])
                i1 += 1
            while i2 < len(right):
                merged.append(right[i2])
                i2 += 1

            new_lists.append(merged)
        else:
            new_lists.append(lists[i])

    lists = new_lists

sorted_list = lists[0]
print("Sorted list:", sorted_list)
