# DataTypes introduction
#
# Use: 
#    python datatypes.py 
# 
from z3 import *

# Algebraic datatypes, offer convenient way for specifying common data structures.
# Record and tuples are special cases of algebraic datatypes, and so are scalars (enumeration)
# But algebraic datatypes are more general. They can be used to specify finite lists, trees, 
# and other recursive structures.

# Phases:
#    1. declare new datatype 
#    2. declare constructors and accessors
#    3. use method create() to create the actual datatype

# We will create a simple data type without recursive nature

## [1] Declare new datatype
MyDataType = Datatype('MyDataType')

## [2] Declare constructors and accessors
# cons1 is a constructor which use an integer ValX to construct the MyDataType
MyDataType.declare('cons1', ('ValX', IntSort()))
# cons2 is a constructor which use integer ValX and ValY to construct the MyDataType
MyDataType.declare('cons2', ('ValX', IntSort()), ('ValY', IntSort()))

# Both constructors are valid.

## [3] Create the datatype
MyDataType = MyDataType.create()


# We can also create alias for the constructors
cons1 = MyDataType.cons1 
cons2 = MyDataType.cons2 
valx  = MyDataType.ValX 
valy  = MyDataType.ValY


# Creating some instance of MyDataType 
Obj1 = cons1(135)
Obj2 = cons2(135, 182)

print('ValX(Obj1) = > {}'.format(simplify(valx(Obj1))))
print('ValX(Obj2) = > {}   ValY(Obj2) => {}'.format(simplify(valx(Obj2)), simplify(valy(Obj2))))