class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)
print(root.data)
print(root.left.left.data)