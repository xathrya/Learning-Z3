# Check the validity of powers of two
#
# Use: 
#    python powers2.py 
# 
from z3 import *

x      = BitVec('x', 32)
powers = [ 2**i for i in range(32) ]
fast   = And(x != 0, x & (x-1) == 0)
slow   = Or([ x == p for p in powers ])
print(fast)
print(slow)

print(fast == slow)