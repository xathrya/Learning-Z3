# Using `simplify` to simplify equations
# 
# Use: 
#    python simplify.py 
# 

from z3 import *

x = Int('x')
y = Int('y')

# simplify() is used to simplify / reduce complex system of equation to simpler one.

#   Declare: simplify(formula)

# Before = x + y + 2*x + 3
# After  = 3 + 3*x + y
print(simplify(x + y + 2*x + 3))

# Before = x < y + x + 2
# After  = Not(y <= -2)
print(simplify(x < y + x + 2))

# Before = And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)
# After  = And(x >= 2, 2*x**2 + y**2 >= 3)
print(simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))

d = BitVecVal(1337, 32)
print(simplify(d << 32))