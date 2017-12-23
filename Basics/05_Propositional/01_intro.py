# Introduction to propositional logic
# 
# Use: 
#    python intro.py 
# 
 
from z3 import *

p, q, r = Bools('p q r')

# Predefined BoolSort is the sort (type) of all Boolean popositional expression.
# Z3 support the usual Boolean operators (see `operator.py` on `Essentials`)

# Demonstrating how to prove "If p implies q and q implies r, then p implies r"
# This is accomplished by showing that the negation is unsatisfiable.

# Create a conjecture
# ((p => q) ^ (q => r)) => (p => r)
conjecture = Implies(And(Implies(p, q), Implies(q, r)), Implies(p,r))
prove(Not(conjecture))

# A formula F is valid if F always evaluates to true for any assignment of 
# appropriate values to its uninterpreted function and constant symbols.

# A formula F is satisfiable if there is some assignment of appropriate values
# to its uninterpreted function and constant symbols under which F evaluates to true.

# Validity is about finding a proof of a statement
# Satisfiability is about finding a solution to a set of constraints.

# Is F valid?
# If F is always true, then Not(F) is alays false. Thus, Not(F) will not have any 
# satisfying assignment, that is F is unsatisfiable.
# Then, F is valid precisely when Not(F) is not satisfiable.