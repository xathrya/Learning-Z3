from z3 import *

x = BitVec('x', 32)
y = BitVec('y', 32)
z = BitVec('z', 32)

# Prove
# Are there any case for x and y where 
# (x xor y) doesn't equals to ((y&x) * -2) + (y + x)

s = Solver()
s.add(x ^ y == z)
s.add(((y & x) * 0xFFFFFFFE) + (y + x) != z)

print(s.check())