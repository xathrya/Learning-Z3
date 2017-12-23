# Substitute component of formula with something else
# 
# Use: 
#    python substitute.py 
# 

from z3 import *

# Substitute a node in expression with something other
a, b = BitVec('a', 32), BitVecVal(1, 32)
x, y = Int('x'), IntVal(1)

# C is an expression built from a and b
print("Expression we have")
c    = a + a + b
z    = x + x + y
print("BitVector: {}".format(c))
print("Int: {}".format(z))

print()

# Substitute a in c will modify the expression but 
# not touching the original
print("Substitute one at a time")
exp1 = substitute(c, (a, BitVecVal(1337, 32)))
exp2 = substitute(z, (x, IntVal(1337)))
print("Original BV: {}".format(c))
print("Substitute: {}".format(exp1))
print("Original INT: {}".format(z))
print("Substitute: {}".format(exp2))

print()

# That way, if we substitute b in c (y in z), it will give 
# different result
exp1 = substitute(c, (b, BitVecVal(135, 32)))
exp2 = substitute(z, (y, IntVal(135)))
print("Original BV: {}".format(c))
print("Substitute: {}".format(exp1))
print("Original INT: {}".format(z))
print("Substitute: {}".format(exp2))

print()

# Multi substitute
print("Substitute multiple variable at a time")
exp1 = substitute(c, (a, BitVecVal(1337, 32)), (b, BitVecVal(135, 32)))
exp2 = substitute(z, (x, IntVal(1337)), (y, IntVal(135)))
print("Original BV: {}".format(c))
print("Substitute: {}".format(exp1))
print("Original INT: {}".format(z))
print("Substitute: {}".format(exp2))

print()

# Substitute with another expression
exp1 = substitute(c, (a, a * b))
exp2 = substitute(z, (x, x * y))
print("Original BV: {}".format(c))
print("Substitute: {}".format(exp1))
print("Original BV: {}".format(z))
print("Substitute: {}".format(exp2))
