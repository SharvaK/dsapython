#create a node
class BTreeNode:
    def __init__(self, leaf = False):
        self.leaf = leaf
        self.keys = []
        self.child = []

#Tree
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    #Insert Node
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0 ,root)
            self.split_child(temp ,0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

        #Insert nonfull
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None,None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
