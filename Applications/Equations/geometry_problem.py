# Solving geometry problem with Z3
#
# Use: 
#    python algebra.py 
# 

from __future__ import print_function
from z3 import *

solver = Solver()

# Represent 4 points (a, b, c, d) in their coordinates
ax = Real("a.x")
ay = Real("a.y")
bx = Real("b.x")
by = Real("b.y")
cx = Real("c.x")
cy = Real("c.y")
dx = Real("d.x")
dy = Real("d.y")

a_c = Real("|a-c|")
b_d = Real("|b-d|")

# The location of some points
solver.add(bx == 0)
solver.add(by == 0)
solver.add(cx == 10)
solver.add(cy == 0)
solver.add(dx == cx)
solver.add(ay == dy)
solver.add(ax == 0)

# BD is on the circle
solver.add(b_d**2 == (bx-dx)**2 + (by-dy)**2)
solver.add(b_d == 20)

solver.add(a_c**2 == (ax-cx)**2 + (ay-cy)**2)


if solver.check() == sat:
  print(solver.model())
else:
  print("Can't solve the problem")
