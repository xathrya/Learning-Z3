#
# Goal: 
#    Solve problem with Real number result
# Use: 
#    python real.py 
# 

from z3 import *

x = Real('x')
y = Real('y')

# Catches: if an equation return real value (non-integer value)
# then an Int variable won't be able to handle it and the system won't
# be satisfied.

solve(x**2 + y**2 > 3, x**3 + y < 5)
