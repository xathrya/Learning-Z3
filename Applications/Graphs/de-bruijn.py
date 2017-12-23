# Reference:
#   https://yurichev.com/blog/de_bruijn/
#   https://chessprogramming.wikispaces.com/De+Bruijn+sequence
#   https://chessprogramming.wikispaces.com/De+Bruijn+Sequence+Generator

from z3 import *

out = BitVec('out', 64)

tmp = []

for i in range(64):
    tmp.append((out >> i) & 0x3F)

s = Solver()

# All overlapping 6-bit chunks must be distinct
s.add(Distinct(*tmp))

# MSB must be zero:
s.add((out & 0x8000000000000000) == 0)

print(s.check())

result = s.model()[out].as_long()
print("0x%x" % result)

# Print overlapping 6-bit chunks:
for i in range(64):
    t = (result >> i) & 0x3F
    print(" " * (63-i) + format(t, 'b').zfill(6))