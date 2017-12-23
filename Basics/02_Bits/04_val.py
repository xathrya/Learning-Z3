# Type conversion in Z3
#   - Convert python to Z3
#   - Convert Z3 type to other Z3 type
# 
# Use: 
#    python val.py 
# 

from z3 import *

x = BitVec('x', 32)

# BitVec, as well as other Z3 primitive types, can be converted to python 
# data type and vice versa. 
# On thing that should be considered is any conversion required integer
# numbers (either from python to Z3 or otherwise)

# To convert from python to Z3
#   Declare: BitvecVal(value, N)
xv = BitVecVal(135, 8)

# To convert back from Z3 to python, use following
# In some case we want the python value back from Z3.
# Some operation will concretize the variable and give it value. However,
# in this case the value is not Python value but rather an instance to some
# Ref. To obtain the value, we need to cast it using the built in function

#   Declare: BVInt(bitvector)
xi = BV2Int(x)

# Note that conversion from value to bitvector is indeed create a BitVec. 
# However, as it is a concrete value makes it capable to be casted directly
print(xv.as_long())
