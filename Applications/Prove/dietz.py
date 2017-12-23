from z3 import *

x = BitVec('x', 64)
y = BitVec('y', 64)
z = BitVec('z', 64)

# Prove
# Dietz's formula is a formula which computing average number of two numbers
# without overflow.
# It is important to find average number of numbers like 0xFFFFFF00 etc using
# 32-bit integers

# on the left:   x + y/2 (or x + y >> 1)
# on the right: Vn e 0..2^64 − 1:(x&y) + (x ⊕ y) >> 1 = x + y >> 1

# We can't operate on 64-bit values on right sides because result will overflow
# So we will zero extend inputs  on right side by 1 bit.

left  = (ZeroExt(1, x) + ZeroExt(1, y)) >> 1
right = ZeroExt( 1, (x&y) + (x ^ y) >> 1 )
f = ForAll([x, y], left == right)
s = Solver()
s.add(f)
print(s.check())