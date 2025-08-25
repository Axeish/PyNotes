# 🌳 Trees in Python: Full Tutorial

## 1. What is a Tree?
A Tree is a hierarchical data structure with the following properties:
- One root node
- Each node has 0 or more children
- No cycles

## 2. Terminology
| Term    | Description                            |
|---------|----------------------------------------|
| Root    | Topmost node of the tree               |
| Node    | An element in the tree                 |
| Leaf    | Node with no children                  |
| Edge    | Connection between parent and child    |
| Height  | Longest path from root to leaf         |
| Depth   | Distance from the root node            |

## 3. Types of Trees
- **General Tree**: Any number of children
- **Binary Tree**: Max 2 children
- **Binary Search Tree (BST)**: Left < Root < Right

## 4. General Tree Implementation
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

        def print_clean_tree(self, prefix="", is_last =True):
        branch= "\u2514\u2500" if is_last else "\u251c\u2500"
        print(prefix+branch+self.data)
        child_prefix =  prefix+ ("  " if is_last else "| ")

        for i, node in enumerate(self.child):
            is_last_c = (i==len(self.child)-1)
            node.print_clean_tree( child_prefix,is_last_c )
```

## 5. Binary Tree Implementation
```python
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

## 6. Tree Traversals
### Inorder (Left → Root → Right)
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
```

### Preorder (Root → Left → Right)
```python
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
```

### Postorder (Left → Right → Root)
```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
```

## 7. Binary Search Tree (BST)
```python
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value == self.data:
            return
        elif value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
```