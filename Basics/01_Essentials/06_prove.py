# Prove or disprove formula(s)
# 
# Use: 
#    python prove.py 
# 
from z3 import *

# The goal is to find whether formulas is proven to be "valid" or not
# Set of formulas is valid if all interpretation exists makes all asserted formulas true.

#   Declare: prove(formula)

# If a formula is valid, it will give verdict "proved"
# If not, it will give a counterexample
a, b = Bools('a b')

# De Morgan Law is true
# (a AND b) = ~(~a OR ~b)
prove(And(a,b) == Not(Or(Not(a), Not(b))))

# Wrong, obviously, but it shows us the capability of giving counterexample
prove(And(a,b) == Or(a,b))