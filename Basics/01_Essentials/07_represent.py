# Expression, arguments, and representation in SMTLIB
#
# Use: 
#    python represent.py 
# 

from z3 import *

x = Int('x')
y = Int('y')

# n is holding expression x + y >= 3
n = x + y >= 3

# in AST (Abstract Syntax Tree) form, it would be:
# n := A >= B
# A := x + y
# B := 3

print("num args: ", n.num_args())       # 2
print("children: ", n.children())       # [x + y, 3]
print("1st child:", n.arg(0))           # x + y       which is another expression
print("2nd child:", n.arg(1))           # 3
print("operator: ", n.decl())           # >=
print("op name:  ", n.decl().name())    # >=
