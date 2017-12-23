# Mix boolean and numbers in single system of equations
#
# Use: 
#    python mix.py 
# 

from z3 import *

p = Bool('p')
x = Real('x')

# This system of equations have two expressions
#    (x < 5) OR (x > 10)
#    p OR (x**2 == 2) OR ~p
#
# => [x = -1.4142135623?, p = False]
solve(Or(x < 5, x > 10), Or(p, x**2 == 2), Not(p))