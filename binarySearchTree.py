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

root = None
for i in range(5):
    decide = int(input("enter value to insert"))
    root = insert(root,decide)
inorderTraversal(root)

