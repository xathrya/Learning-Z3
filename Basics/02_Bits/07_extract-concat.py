# Extract and concat bits of vectors
# 
# Use: 
#    python exextract-concat.py 
# 

from z3 import *

# Creating 
a = BitVecVal(0xdead, 16)
b = BitVecVal(0xbe, 8)
c = BitVecVal(0xef, 8)

# Concatenation
# Concatenate some bitvectors to a new value which every of them are joined
# together in respect to the order of argument.
#   Declare: Concat(h, l, x)
d = Concat(a, b, c)
print(simplify(d))
print(hex(3735928559))

#   Declare: Extract(h, l, x)


e = Extract(31, 16, d)
print(simplify(e), hex(57005))
print(d.size())