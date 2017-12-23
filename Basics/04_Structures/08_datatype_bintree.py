# Binary Tree as an example of Data Type
#
# Use: 
#    python datatype_bintree.py 
# 
from z3 import *

# See also datatype.py 

s = Solver()

### Declare binary tree data type 
BinaryTree = Datatype('BinaryTree')

# Leaf is a value only node
BinaryTree.declare('leaf', ('value', IntSort()))

# The typical node in binary tree is a value and two successor
BinaryTree.declare('node', ('value', IntSort()), ('left', BinaryTree), ('right', BinaryTree))

# Create the data type
# Using method create() to create the actual datatype
BinaryTree = BinaryTree.create()


# Creating alias
leaf  = BinaryTree.leaf
node  = BinaryTree.node
value = BinaryTree.value
left  = BinaryTree.left
right = BinaryTree.right


# Creating an instance of a binary tree
t = node(2, (leaf(0)), (leaf(1)))

print('simplify(value(t)) => {}'.format(simplify(value(t))))
print('simplify(value(left(t))) => {}'.format(simplify(value(left(t)))))