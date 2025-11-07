'''#31/10/25

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def inorder(root):
    if root.leftNode != None:
        inorder(root.leftNode)
    print(root.data)
    if root.rightNode != None:
        inorder(root.rightNode)

root = TreeNode(12)
root.leftNode = TreeNode(8)
root.rightNode = TreeNode(15)
root.leftNode.leftNode = TreeNode(2)
root.leftNode.rightNode = TreeNode(9)
root.rightNode.leftNode = TreeNode(14)
root.rightNode.rightNode = TreeNode(19)
inorder(root)




'''


# 31/10/25

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def inorder(root):
    if root:
        inorder(root.leftNode)
        print(root.data, end=' ')
        inorder(root.rightNode)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.leftNode)
        preorder(root.rightNode)

def postorder(root):
    if root:
        postorder(root.leftNode)
        postorder(root.rightNode)
        print(root.data, end=' ')

#Construct tree
root = TreeNode(12)
root.leftNode = TreeNode(8)
root.rightNode = TreeNode(15)
root.leftNode.leftNode = TreeNode(2)
root.leftNode.rightNode = TreeNode(9)
root.rightNode.leftNode = TreeNode(14)
root.rightNode.rightNode = TreeNode(19)

print("Inorder traversal:")
inorder(root)
print("\nPreorder traversal:")
preorder(root)
print("\nPostorder traversal:")
postorder(root)
