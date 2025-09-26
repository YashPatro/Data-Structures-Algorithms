#26/09/25

#l_bound

l = [1,2,5,6,6,6,7,7,7,7,7,7,9,9]

n = int(input('Enter Value: '))

def l_bound(n,l):
    low,high = 0,len(l)-1
    while low < high:
        mid = (low+high)//2
        if n > l[mid]:
            low = mid+1
        else:
            high = mid
    # print(low)
    return low


lb = l_bound(n,l)
print(lb)

#upper bound

def upper(n,l):
    low,high = 0,len(l)-1
    while low < high:
        mid = (low+high)//2
        if n >= l[mid]:
            low = mid+1
        else:
            high = mid
    # print(low)
    return low


ub2 = upper(n,l)
print(ub2)
print(f'you have {ub2-lb} occurences of {n}')