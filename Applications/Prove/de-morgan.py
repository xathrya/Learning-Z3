from z3 import *

p, q = Bools('p q')

# Prove the De Morgan
left  = And(p,q)
right = Not(Or(Not(p), Not(q)))
demorgan = left == right
print(demorgan)

print("Proving de Morgan")
prove(demorgan)