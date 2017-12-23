# 3x + 2y - z  = 1
# 2x - 2y + 4z = -2
# -x + y/2 - z = 0

from z3 import *

x = Real('x')
y = Real('y')
z = Real('z')

s = Solver()

s.add(3*x + 2*y - z == 1)
s.add(2*x - 2*y + 4*z == -2)
s.add(-x + y/2 - z == 0)

print(s.check())
print(s.model())