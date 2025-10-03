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