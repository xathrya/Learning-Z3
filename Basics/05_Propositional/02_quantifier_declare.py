# Declaring quantified expression
#
# Use: 
#    python quantifier_declare.py 
# 

from z3 import *

# for syntactic sugar only
IS = IntSort()

x, y = Ints('x y')
a, b = Ints('a b')

f = Function('f', IS, IS, IS)

# Z3 can solve quantifier-free problems containing arithmetic, bitvector, booleans, arrays,
# functions, and datatypes. It can also accepts and work with formulas that use quantifiers.
# It is no longer a decision procedures for such formula in general.

# For All instance, do this
#   ForAll(A, B)
#   A => variables involved
#   B => expression
fa = ForAll([x, y], f(x, y) == 0)
print(fa)

# There exists interpretation that satisfy this
#   Exists(A, B)
#   A => variables involved
#   B => expression
te = Exists(x, f(x, x) >= 0)
print(te)

solve(ForAll(x, f(x,x) == 0), f(a,b) == 1)

# constants x and y were used to create quantified formulas.
# This is a trick for simplifying the construction of quantified formulas in Z3Py.
# internally these constants are replaced by bounded variables.

print()

# body() retrieves the quantified expression.
print("Body  => {}".format(fa.body()))
v1 = fa.body().arg(0).arg(0)
print("A0.A0 => {}".format(v1))

# Var(index, sort) creates a bounded/free variables with the given index and sort
print(eq(v1, Var(1, IS)))