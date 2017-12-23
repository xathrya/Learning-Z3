# Rotate the bit vectors
# 
# Use: 
#    python extends.py 
# 
from z3 import *

x = BitVecVal(1, 32)

# Rotate in essence is similar to shifting but the overflowed characters 
# are pushed back to the opposite of shift direction.

print(simplify(RotateRight(x, 1)))
print(hex(2147483648))

print(simplify(RotateLeft(x, 1)))