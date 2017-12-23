# Break the insecure hash generation algorithm
#
# Use: 
#    python easyhash1.py 
# 
import random
from z3 import *

# The hash algorithm has a weak algorithm which can be decomposed as a series of operations

# The hash function
def hash(s):
    h = 0x4E67CA67
    for i,c in enumerate(s):
        a = (h >> 2) & 0xFFFFFFFF
        b = (h << 5) & 0xFFFFFFFF
        h = h ^ (a + b + ord(c))
        h &= 0xFFFFFFFF
    return h

# Helper function
def shr32(v, n):
    return (v >> n) & ((1 << (32 - n)) - 1)

solver = Solver()

# Create random value, the hash should has this value as result so what is the data before?
htest = random.randint(0, 1<<32 - 1)
print(hex(htest))

xs = list(BitVecs('c0 c1 c2 c3 c4 c5', 32))

h = BitVec('hs', 32)
solver.add(h == 0x4E67CA67)

for i, c in enumerate(xs):
    solver.add(0 <= c, c < 255)
    h = h ^ (shr32(h, 2) + (h << 5) + c)

solver.add(h == htest)

print(solver.check())
if solver.check() == sat:
    m = solver.model()
    s = "".join( [ chr( m[c].as_long() ) for c in xs ] )
    print(s.encode())
    print(hex(hash(s)))