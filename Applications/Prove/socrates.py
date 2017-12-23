from z3 import *

Object = DeclareSort('Object')

Human  = Function('Human', Object, BoolSort())
Mortal = Function('Human', Object, BoolSort())

# a well known philasopher
socrates = Const('socrates', Object)

# free variables used in forall be declared Const in python
x = Const('x', Object)

axioms = [ ForAll([x], Implies(Human(x), Mortal(x))), Human(socrates) ]

s = Solver()
s.add(axioms)

while s.check() == sat:
    m = s.model()
    print(m)

    # classical refutation
    s.add(Not(Mortal(socrates)))