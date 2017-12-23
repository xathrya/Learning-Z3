# Declare bitvectors
# 
# Use: 
#    python declare.py 
# 
 
from z3 import *

# Bit Vector is used for machine arithmetic
# Usually model CPU register or memory 

# Creating bitvector of 8 bit => 256 different values
bv1 = BitVec('bv1', 8)

# Creating bitvector of 32 bit => 2**32 different values
bv2 = BitVec('bv2', 32)

# BitVector from value
bv3 = BitVecVal(0xDEAD, 16)

# bv4 and bv5 is equal
bv4 = BitVecVal(-1, 16)
bv5 = BitVecVal(65535, 16)
print(bv4 == bv5)
print(simplify(bv4 == bv5))

# bv6 and bv7 is not equal
bv6 = BitVecVal(-1, 32)
bv7 = BitVecVal(65535, 32)
print(bv6 == bv7)
print(simplify(bv6 == bv7))
