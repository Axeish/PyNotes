#Binary Tree operation Python
'''
Binary tree is used where we need to 
-manipulate hierarchial data structure like directory 
- manipulate sorted data


Tree provide quicker access/search , than Linked List and slower than arrays
Tree provide quicker insert/deletion tha arrays and slowere than unordered linked list 
'''



'''
Creating Root 

'''

class Node:
	def __init__(self, data):
		self.left = None
		self.right= None
		self.data = data
	def show_tree (self):
		if self.left:
			self.left.show_tree()
		print(self.data)
		if self.right:		
			self.right.show_tree()
class Operation:
	def invertTree(self,root):
		if root:
			root.left, root.right=root.right, root.left
			self.invertTree(root.left)
			self.invertTree(root.right)
		return root	



root = Node(10)
b=Node(15)
c=Node(19)
d=Node(5)
e=Node(59)
d.left=e
d.right=c
root.left=b
root.right=d

root.show_tree()


oper=Operation()
inver =oper.invertTree(root)
inver.show_tree()
