#12/09/2025

import random,string

l = [random.randint(1,50) for i in range(10)]
l.append(10)
print(l.index(10))
a = [random.choice(string.printable) for i in range(15)]
# f = False
def linear():
    print(l)
    f  = False
    n = int(input('enter number: '))
    for i,v in enumerate(l):
        if n == v:
            f = True
            break
    if f:
        print(f'value found at {i}')   
    else:
        print('value not found')     

linear()

#recursive

def l_search(x,n):
    if x == n:
        print(f'{n} found! at{l.index(x)}')
        return True 
        
    else:
        return False 
n = int(input('enter num: '))
for i in l:
    result = l_search(i,n) 
    if result:
        break
print(result)

# hw
import random, string

a = [random.choice(string.ascii_letters) for i in range(15)]

def linear():
    print(a)
    f = False
    n = input('enter string: ')
    for i,v in enumerate(a):
        if n == v:
            f = True
            break
    if f:
        print(f'value found at {i}')   
    else:
        print('value not found')     

linear()

def l_search(x,n):
    if x == n:
        print(f'{n} found! at {a.index(x)}')
        return True 
    else:
        return False 

n = input('enter string: ')
for i in a:
    result = l_search(i,n) 
    if result:
        break
print(result)
