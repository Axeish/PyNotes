class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []

    def add_child(self, child_node):
        self.child.append(child_node)

    def print_clean_tree(self, prefix="", is_last =True):
        branch= "\u2514\u2500" if is_last else "\u251c\u2500"
        print(prefix+branch+str(self.data))
        child_prefix =  prefix+ ("  " if is_last else "| ")

        for i, node in enumerate(self.child):
            is_last_c = (i==len(self.child)-1)
            if node:
                node.print_clean_tree( child_prefix,is_last_c )

class BSTNode(TreeNode):
    def __init__(self, data:int):
        self.data =data
        self.left = None
        self.right = None
    @property
    def child(self):
        res =[]
        if self.left:
            res.append(self.left)
        if self.right:
            res.append(self.right)
        return res

    def add_child(self, node):
        if node.data == self.data:
            return #avoid duplicate
        if node.data > self.data:
            if self.right :
                self.right.add_child(node)
            else:
                self.right=node
        if node.data < self.data:
            if self.left:
                self.left.add_child(node)
            else:
                self.left=node

#find max depth of a tree

def max_node(node):
    if not node:
        return 0
    return 1+ max(max_node(node.left),max_node(node.right))



root = BSTNode(40)
root.add_child(BSTNode(5))
root.add_child(BSTNode(55))
root.add_child(BSTNode(255))
root.add_child(BSTNode(15))
root.add_child(BSTNode(25))
root.add_child(BSTNode(2))
root.add_child(BSTNode(45))
root.add_child(BSTNode(20))
root.add_child(BSTNode(17))


root.print_clean_tree()
print(max_node(root))

