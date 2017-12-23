# Nonlinear arithmetic in Z3Py
# 
# Use: 
#    python nonlinear.py 
# 
 
from z3 import *

a = Int('a')
b, c, d = Reals('b c d')

def check(formula):
    s = Solver()
    s.add(formula)
    t = s.check()
    print(t)
    if t == sat:
        print(s.model())

# A formula is nonlinear if it contains expression of the form `t * s`, or (* t s) in SMTLIB2,
# where t and s are not numbers.
# Nonlinear real arithmetic is very expensive and Z3 is not complete for this kind of formula.
# Nonlinear integer arithmetic is undecideable: there is no correct and terminates (for every input)
# with sat or unsat answer.
# It doesn't prevent Z3 from returning an answer for many nonlinear problems. The real limit is
# that there will always be a nonlinear integer arithmetic formula that it will fail produce an answer

f = a * a > 3
check(f)

print("Z3 does not always find solutions to non-linear problems")
f = b * b * b + b*c == 3.0
check(f)

print("yet it can show unsatisfiability for some nontrivial nonlinear problems.")
f = []
f.append( b * b == (b + 2.0) )
f.append( b * c == b )
f.append( (c - 1.0)*d == 1.0 )
check(f)

print("when presented only nonlinear constraints over reals, Z3 uses a specialized complete solver")
f = b * b * b + b * c == 3.0
check(f)