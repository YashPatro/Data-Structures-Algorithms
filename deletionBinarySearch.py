'''#14/11/25
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def insert(root,value):
    if root == None:
        return TreeNode(value)
    if value < root.data:
        root.leftNode = insert(root.leftNode,value)
    else:
        root.rightNode = insert(root.rightNode,value)
    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.leftNode)
        print(root.data)
        inorderTraversal(root.rightNode)

def successor(root):
    c = root
    while c.leftNode:
        c = c.leftNode
    return c

def delete(root,val):
    if root == None:
        return root
    print("checking:", root.data)
    if val < root.data:
        print("going left")
        root.leftNode = delete(root.leftNode,val)
    elif val > root.data:
        print("going right")
        root.rightNode = delete(root.rightNode,val)
    else:
        print("found:", root.data)
        if root.leftNode == None:
            temp = root.rightNode
            root = None
            return temp
        elif root.rightNode == None:
            temp = root.leftNode
            root = None
            return temp
        temp = successor(root.rightNode)
        print("successor:", temp.data)
        root.data = temp.data
        root.rightNode = delete(root.rightNode,temp.data)
    return root

root = None
for i in range(5):
    decide = int(input("enter value to insert "))
    root = insert(root,decide)

print("inorder traversal:")
inorderTraversal(root)

removal = int(input("enter value to delete "))
root = delete(root,removal)

print("inorder after deletion:")
inorderTraversal(root)'''
#14/11/25

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None
    def abc(self):
        print('abc')
    def xyz(self):
        self.abc()

def inorderTraversal(root):
    if root:
        if root.leftNode:
            inorderTraversal(root.leftNode)
        print(root.data)
        if root.rightNode:
            inorderTraversal(root.rightNode)
def insert(root,value):
    if root is None:
        return TreeNode(value)
    if root.data > value:
            root.leftNode = insert(root.leftNode,value)

    else:
        root.rightNode = insert(root.rightNode,value)
    return root
def successor(root):
    c = root 
    while c.leftNode:
        c = c.leftNode
    return c 

def delete(root,val):
    if root:
        if root.data > val:
            root.leftNode = delete(root.leftNode,val)
        elif root.data < val:
            root.rightNode = delete(root.rightNode,val)
        else:
            #root has only one (left) child
            if root.leftNode  is None:
                temp = root.rightNode 
                root = None
                return temp
            elif root.rightNode is None:
                temp = root.leftNode
                root = None 
                return temp
            else:
                temp = successor(root)
                print(temp.data)   
                a = root.data 
                root.data = temp.data  
                temp.data = a 
                root.rightNode = delete(root.rightNode,temp.data)
                print(a)

   

root = None

for i in range(5):
    decide = int(input("enter value to insert"))
    root = insert(root,decide)
    
inorderTraversal(root)
removal = int(input('enter number for removal'))
delete(root,removal)
inorderTraversal(root)

