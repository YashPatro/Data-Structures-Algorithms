open = ['(','[','{']
closed = [')',']','}']

def checking(exp):
    stack = []
    for i in exp:
        if i in open:
            stack.append(i)
        elif i in closed :
            if len(stack) != 0:
                pos = closed.index(i)
                if open[pos] == stack[-1]:
                    stack.pop()
                else:
                    return "invalid/imbalanced expression"
    if len(stack) == 0:
        return "valid expression"
    else:
        return "invalid brackets"

exp = "(a+b(([)]]))"
print(checking(exp))