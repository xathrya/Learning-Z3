# Introduction to signed and unsigned operator
#
# Use: 
#    python hello.py 
# 
from z3 import *

a = BitVec('a', 8)
s = Solver()

# Signed operator
s.add(a < 0)
print(s.check())
print(s.model())

s.reset()

# Unsigned operator
# ULT = Unsigned Less Than
# UGT = Unsigned Greater Than
# ULE = Unsigned Less-than / Equal
# UGE = Unsigned Greater-than / Equal
s.add(ULT(a, 0))
print(s.check())