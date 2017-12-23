# Expand the bit vectors
# 
# Use: 
#    python extends.py 
# 
 
from z3 import *

x = BitVec('x', 16)
y = BitVec('y', 32)

# Two bitvectors is operable under the operator if it they have same amount
# of bits. If they have different amount of bits, we should extends one of them.
# Extends is expanding the bits, adding N bits to the vectors.

# Extend the bit vector by adding 10 bits in front.
# Therefore the total bit would be 16 + 10 = 26
print(x.size())
zx = ZeroExt(10, x)
print(zx.size())

print()

# Extend the bit vector by adding 4 bits in front
# Therefore the total bit would be 32 + 4 = 36
print(y.size())
sy = SignExt(4, y)
print(sy.size())

# Compare the values
# The ZeroExt will fill the extended bits with 0, regardless of the sign.
# The SignExt will keep the signness
ze = ZeroExt(24, BitVecVal(-1, 8))
se = SignExt(24, BitVecVal(-1, 8))
print(hex(simplify(ze).as_long()))
print(hex(simplify(se).as_long()))