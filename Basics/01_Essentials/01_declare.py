# Declare variables and solve equation
#
# Use: 
#    python declare.py 
# 

from z3 import *

# Z3 has "type system" and "variables" to hold a "value".
# They are bound by constrained in which Z3 try to prove and assign certain value to
# these variables, which satisfy the constraints.
# the string is internal name representation of variable, which will be feed to Z3

# Integer
#   Declare: Int('varname')
a = Int('a')            # unbound by machine, can be any integer value
b = Int('b')
a_, b_ = Ints('a_ b_')  # declare multiple Ints on single line

# Real
#   Declare: Real('varname')
c = Real('c')           # unbound by machine, can be any real value
d = Real('d')
c_, d_ = Reals('c_ d_') # declare multiple Reals on single line

# Bool
#   Declare: Bool('varname')
e = Bool('e')
f = Bool('f')
e_, f_ = Bools('e f')

# Vectors
# the bit vectors, more on 3_Bits
#   Declare: BitVec('varname', N)
g = BitVec('g', 32)         # a 32-bit variable
h = BitVec('h', 16)         # a 16-bit variable
i = BitVec('i', 11)         # a 11-bit variable
g_, h_ = BitVecs('g_ h_', 32)   # declare multiple bitvector of similar length (32 in this case)

# integer vectors
#   Declare: IntVectors('varname', N)
j = IntVectors('j', 10)     # create a vector of 10 ints

# real vectors
#   Declare: RealVectors('varname', N)
k = RealVectors('k', 10)    # create a vector of 10 reals

# using list comprehension
xs = [ Bool("x%d" % i) for i in range(128) ]