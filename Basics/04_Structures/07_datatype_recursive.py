# A mutually recursive data type
#
# Use: 
#    python datatype_recursive.py 
# 
from z3 import *

# See also datatype.py 

### Declare a Mutually Recursive Datatypes
TreeList = Datatype('TreeList')
Tree     = Datatype('Tree')

# There is a tree, has only two branch namely left and right.
# Each branch is a list of tree.

# Declaration for Tree
Tree.declare('leaf', ('val', IntSort()))
Tree.declare('node', ('left', TreeList), ('right', TreeList))

# Declaration for TreeList
TreeList.declare('nil')
TreeList.declare('cons', ('car', Tree), ('cdr', TreeList))

# Crate the data type for multiple recursive datatype
Tree, TreeList = CreateDatatypes(Tree, TreeList)


t1  = Tree.leaf(10)
t11 = TreeList.cons(t1, TreeList.nil)
t2  = Tree.node(t11, TreeList.nil)
print(t2)
print(simplify(Tree.val(t1)))

t1, t2, t3 = Consts('t1 t2 t3', TreeList)
solve(Distinct(t1, t2, t3))