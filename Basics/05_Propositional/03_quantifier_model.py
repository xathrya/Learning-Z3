# Using model of quantified expression
#
# Use: 
#    python quantifier_model.py 
# 

from z3 import *

## Modelling with Quantifier
# Suppose we want to model an object-oriented type with single inheritance.
# We need a predicate for sub-typing. Sub-typing should be a partial-order and respect
# single inheritance.
# For some built-in type constructor such as for `array_of`, subtyping should be monotone
Type     = DeclareSort('Type')
subtype  = Function('subtype', Type, Type, BoolSort())
array_of = Function('array_of', Type, Type)
root     = Const('root', Type)

x, y, z  = Consts('x y z', Type)

axioms   = [ ForAll(x, subtype(x, x)), 
             ForAll([x, y, z], Implies(And(subtype(x, y), subtype(y, z)), subtype(x, z))),
             ForAll([x, y],    Implies(And(subtype(x, y), subtype(y, x)), x == y)),
             ForAll([x, y, z], Implies(And(subtype(x, y), subtype(x, z)), Or(subtype(y, z), subtype(z, y)))),
             ForAll(x, subtype(root, x))
           ]

s = Solver()
s.add(axioms)

print("The axioms we have: ")
print(s)
print(s.check())

print()

print("Interpretation for Type: ")
print(s.model()[Type])

print()

print("Model: ")
print(s.model())