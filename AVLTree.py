#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		

	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key=key

	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value=value


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left=node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right=node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent=node

	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height=h


	"""sets the size of node

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size=s


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if self.key!= None:
			return True
		else:
			return False

	def bf(self):
		left_son_hight=self.get_left().get_height()
		right_son_hight=self.get_right().get_height()
		return (left_son_hight-right_son_hight)

	def set_virtual_sons(self):
		self.set_left(AVLNode(None, None))
		self.get_left().set_parent(self)
		self.set_right(AVLNode(None, None))
		self.get_right().set_parent(self)
"""
A class implementing an AVL tree.
"""





class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root =AVLNode(None,None)




	"""searches for a value in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: any
	@returns: the value corresponding to key.
	"""
	def search(self, key):
		node=self.root
		while node.is_real_node()==True:
			if node.get_key()==key:
				return node
			elif node.get_key()<key:
				node=node.get_left()
			elif node.get_key()>key:
				node = node.get_right()
		return None

	def left_to_right_roll(self,node_l,node_r):
		node_r.set_left(node_l.get_right())
		node_r.get_left().set_parent(node_r)
		node_l.set_right(node_r)
		node_l.set_parent(node_r.get_parent())
		if node_l.get_parent()!=None:
			if node_l.get_parent().get_left()==node_r:
				node_l.get_parent().set_left(node_l)
			else:
				node_l.get_parent().set_right(node_l)
		else:
			self.root=node_l
		node_r.set_parent(node_l)
		return node_l

	def right_to_left_roll(self,node_l,node_r):
		node_l.set_right(node_r.get_left())
		node_l.get_right().set_parent(node_l)
		node_r.set_left(node_l)
		node_r.set_parent(node_l.get_parent())
		if node_r.get_parent()!=None:
			if node_r.get_parent().get_left()==node_l:
				node_r.get_parent().set_left(node_r)
			else:
				node_r.get_parent().set_right(node_r)
		else:
			self.root=node_r
		node_l.set_parent(node_r)
		return node_r
	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		num_of_rotaions=0
		node = self.root
		while node.is_real_node()==True:
			if node.get_key()<key:
				node.set_size(node.get_size()+1)
				node=node.get_right()
			elif node.get_key()>key:
				node.set_size(node.get_size() + 1)
				node = node.get_left()
		node.set_key(key)
		node.set_value(val)
		node.set_height(0)
		node.set_virtual_sons()
		y=node.get_parent()
		while y!=None:
			perent_height_after=1+max(y.get_right().get_height(),y.get_left().get_height())
			if perent_height_after==y.get_height():
				return num_of_rotaions
			y.set_height(perent_height_after)
			if -1>y.bf() or y.bf()>1:
				if y.bf()==2:
					if y.get_left().bf()==1:
						y=self.left_to_right_roll(y.get_left(), y)
						y.get_right().set_height(y.get_right().get_height()-2)
						num_of_rotaions+=1
					if y.get_left().bf()==-1:
						y.set_height(y.get_height()-2)
						y.get_left().set_height(y.get_left().get_height()-1)
						y.get_left().get_right().set_height(y.get_left().get_right().get_height()+1)
						l_node_after_roll = self.right_to_left_roll(y.get_left(), y.get_left().get_right())
						y = self.left_to_right_roll(l_node_after_roll, y)
						num_of_rotaions += 2
				if y.bf()==-2:
					if y.get_right().bf()==-1:
						y=self.right_to_left_roll(y,y.get_right())
						y.get_left().set_height(y.get_left().get_height()-2)
						num_of_rotaions += 1
					if y.get_right().bf()==1:
						y.set_height(y.get_height() - 2)
						y.get_right().set_height(y.get_right().get_height() - 1)
						y.get_right().get_left().set_height(y.get_right().get_left().get_height() + 1)
						r_node_after_roll=self.left_to_right_roll(y.get_right().get_left(), y.get_right())
						y=self.right_to_left_roll(y,r_node_after_roll)
						num_of_rotaions+=2
			y=y.get_parent()
		return num_of_rotaions
	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		return -1


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.get_root().get_size()	

	
	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None

	
	"""joins self with key and another AVLTree

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree, key, val):
		return None


	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		return None


	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return None
	"""================================================delate============================================"""

	def printt(self):
		out = ""
		for row in self.printree(self.root):  # need printree.py file
			out = out + row + "\n"
		print(out)

	def printree(self, t, bykey=True):
		# for row in trepr(t, bykey):
		#        print(row)
		return self.trepr(t, False)

	def trepr(self, t, bykey=True):
		if t == None:
			return ["#"]
		thistr = str(t.key)
		return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))

	def conc(self, left, root, right):
		lwid = len(left[-1])
		rwid = len(right[-1])
		rootwid = len(root)
		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]
		ls = self.leftspace(left[0])
		rs = self.rightspace(right[0])
		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid *
					  " " + "\\" + rs * "_" + (rwid - rs) * " ")
		for i in range(max(len(left), len(right))):
			row = ""
			if i < len(left):
				row += left[i]
			else:
				row += lwid * " "
			row += (rootwid + 2) * " "
			if i < len(right):
				row += right[i]
			else:
				row += rwid * " "
			result.append(row)
		return result

	def leftspace(self, row):
		# row is the first row of a left node
		# returns the index of where the second whitespace starts
		i = len(row) - 1
		while row[i] == " ":
			i -= 1
		return i + 1

	def rightspace(self, row):
		# row is the first row of a right node
		# returns the index of where the first whitespace ends
		i = 0
		while row[i] == " ":
			i += 1
		return i

	"""========================================================================================================"""

tree=AVLTree()
tree.insert(12,12)
tree.insert(13,12)
tree.insert(14,12)
tree.insert(15,12)
tree.insert(16,12)
tree.insert(17,12)
tree.insert(1,12)
tree.insert(2,12)
tree.insert(3,12)
tree.printt()