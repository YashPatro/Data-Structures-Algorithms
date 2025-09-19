#19/09/25
import random
l = [random.randint(0,20) for i in range(20)]
l.sort(reverse = False)

print('list: ',l)

start_i = 0
end_i = len(l)-1
middle_i = (start_i+end_i)//2
n = int(input('Enter Number from List: '))
found = False
while start_i <= end_i:
    middle_i = (start_i+end_i)//2
    print(start_i,middle_i,end_i)
    if l[middle_i] == n:
        found = True
        break
    elif l[middle_i] > n:
        end_i = middle_i-1
    elif l[middle_i] <n: 
        start_i = middle_i+1

# if found:
#     print(f'Value found at {middle_i+1}th place')
# else:
#     print('Value not in list')

def find(s,e,k):
    m = (s+e)//2
    if s <= e:
        if k == l[m]:
            return m
        elif k < l[m]:
            return find(s,m-1,k)
        else:
            return find(m+1,e,k)
    else:
        return -1
result = find(0,len(l)-1,n)
if result:
    print(f'value found at {result}')
else:
    print('value not found')

            