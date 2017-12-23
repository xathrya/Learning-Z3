# Simple list as an example of Datatype 
#
# Use: 
#    python datatype_list.py 
# 
from z3 import *

# see also datatype.py

### Declare list of integers data type
List = Datatype('List')

# Constructor cons: (Int, List) -> List 
# A recursive structure, similar as in LISP
#    cons = constructor
#    car  = accessor (head)
#    cdr  = accessor (tail)
List.declare('cons', ('car', IntSort()), ('cdr', List))

# Constructor nil: List
List.declare('nil')

# Create the data type
# Using method create() to create the actual datatype
List = List.create()


# Creating alias
cons = List.cons
car  = List.car
cdr  = List.cdr 
nil  = List.nil


# cons, car, and cdr are function declaration while nil is a constant
print("is_sort? {}".format(is_sort(List)))
print("is_func_decl? {}".format(cons))
print("is_expr? {}".format(is_expr(nil)))

# l1 = [10, 20]
# l2 = [30]
l1 = cons(10, cons(20, nil))
l2 = cons(30, nil)

print()

print("l1 is: {}".format(l1))

print()

print("simplify(cdr(l1))   => {}".format(simplify(cdr(l1))))
print("simplify(cdr(l1))   => {}".format(simplify(cdr(l1))))
print("simplify(l1 == nil) => {}".format(simplify(l1 == nil)))