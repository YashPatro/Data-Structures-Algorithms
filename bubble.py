# 03/10/25

import random

l = [random.randint(1,20) for _ in range(10)]

print(l)

# sorted = l.sort()
# print(l)
# sorted2 = l.sort(reverse = True)
# print(l)
# # sorting 
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         print(i,j)
#         if l[i] > l[j]:
#             l[i],l[j] = l[j],l[i]
        
# print(l)
# actual bubble sort
count = 0
l1 = l
n = len(l)
for i in range(len(l)):
    swap = False
    for j in range(n-i-1):
        print(i,j)
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
            swap = True
        count+=1
    # if swap == False:
    #     break
print(count)
print(l)
print(l1)
count = 0
n = len(l1)
for i in range(len(l1)):
    swap = False
    for j in range(n-i-1):
        print(i,j)
        if l1[j] > l1[j+1]:
            l1[j],l1[j+1] = l1[j+1],l1[j]
            swap = True
        count+=1
    # if swap == False:
    #     break
print(count)
print(l1)


import random

l = [random.randint(1, 20) for _ in range(10)]
print("Original list:", l)

def bubble_sort(l_input):
    l_copy = l_input.copy()
    count = 0
    loops = 0
    n = len(l_copy)

    for i in range(n):
        swap = False
        loops += 1
        for j in range(n - i - 1):
            count += 1
            if l_copy[j] > l_copy[j + 1]:
                l_copy[j], l_copy[j + 1] = l_copy[j + 1], l_copy[j]
                swap = True
        if not swap:
            break

    print("\n--- Bubble Sort ---")
    print("Sorted list:", l_copy)
    print("Comparisons (count):", count)
    print("Loops (passes):", loops)

def insertion_sort(l_input):
    l_copy = l_input.copy()
    count = 0

    for i in range(1, len(l_copy)):
        key = l_copy[i]
        j = i - 1
        while j >= 0 and l_copy[j] > key:
            l_copy[j + 1] = l_copy[j]
            j -= 1
            count += 1
        count += 1
        l_copy[j + 1] = key

    print("\n--- Insertion Sort ---")
    print("Sorted list:", l_copy)
    print("Comparisons (count):", count)

bubble_sort(l)
insertion_sort(l)
