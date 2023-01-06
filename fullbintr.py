class Node:

    def __init__(self, item ) :
        self.item = item
        self.leftChild = None
        self.rightChild = None

#Check if the tree is full binary tree
def isFullTree(root):

    #Tree is empty case
    if root is None:
        return True

    #Check whether tree has child node
    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))    
    return False

root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.rightChild.leftChild = Node(7)
root.leftChild.rightChild.rightChild = Node(6)


if isFullTree(root):
    print("It is a full binary tree")
else:
    print("It is not a full binary tree")



    

        