# Using simple If-Then-Else construction
#
# Use: 
#    python if-then-else.py 
# 
from z3 import *

# Z3 support conditional / branching.
# Unlike some programming language, Z3 (and SMTLIB2) only support "If-Then-Else"
# form. It means a branching is either happen to action when condition met or
# otherwise.
a_, b_ = BitVecs('a_ b_', 32)

# If(condition, ACTION_IF_TRUE, ACTION_IF_FALSE)
a = If(ULT(a_ + b_, 100), a_ + BitVecVal(100, 32), BitVecVal(1337, 32))      # this will return expression based on condition ULT(a_ + b_, 100)
b = If(ULT(a_ + b_, 100), b_ - BitVecVal(10, 32), b_ + BitVecVal(1000, 32))  # this will return expression based on condition ULT(a+ + b_, 100)

solve(UGT(a, 1337), b == 0xdeadbeef)