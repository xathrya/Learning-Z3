#
# Goal: 
#    Representation of BitVector
# Use: 
#    python represent.py 
# 
 
from z3 import *

x = BitVec('x', 16)
y = Bitvec('y', 16)

# Print the expression
print(x + 2)

# Print the internal representation (in SMTLIB)
print((x + 2).sexpr())

# -1 is equal to 65535 for 16-bit integer
print(simplify(x + y -1))

