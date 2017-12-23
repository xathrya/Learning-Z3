# Introduction to Z3Py script
#
# Use: 
#    python hello.py 
# 
 
from z3 import *

# Enumerate all combinations of a and b such that
# the sum of them equal 1337
# We will use solver (see solve and solver) to check
# the satisfiability of formulas.

a, b = BitVecs('a b', 32)
s = Solver()
s.add((a + b) == 1337)
#if s.check() == sat:
#    print(s.model())
#else:
#    print('Unsat')
while s.check() == sat:
    m = s.model()
    print(m)
    s.add(Or(a != m[a], b != m[b]))