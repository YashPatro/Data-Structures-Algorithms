#01/09/25

def factorial(num):
    t =  1
    for i in range(1,num+1):
        t = t*i
    print(t)

factorial(10)


def f_recursion(n):
    if n == 1:
        return 1
    else:
        return n*f_recursion(n-1)
    
def write(n):
    if n == 1:
        print('1\nHappy New Year!!!')
    else:
        print(n)
        write(n-1)

write(10)

def items(l):
    if not l:
        return 0
    else:
        
        return l[0]+items(l[1:])
l1 = [1,2,3,4,5]

print(items(l1))

#fibonacci sequnce / hw
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(7):
    print(fibonacci(i))
