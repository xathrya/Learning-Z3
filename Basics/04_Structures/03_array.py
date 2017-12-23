# Array definition and usage
#
# Use: 
#    python array.py 
# 
from z3 import *

x, y = Ints('x y')

# Theoretical "array" in mathematical theory of computation.
# Array is characterized by the select-store axioms.
#
# Axioms:
#    Select(a, idx)         returns the value stored at position `idx` of the array `a`
#    Store(a, idx, val)     store the value `val` on array on index `idx`, return new array
#                           identical to a but on position `idx` it contains the value val

# By default Z3 assumes that arrays are extensional over select.
# Z3 also enforces that if two arrays agree on all reads then the arrays are equal.

# Aliasing sorts
IS  = IntSort()
BV8 = BitVecSort(8)
BV32= BitVecSort(32)

#### Define an array
# similar to arr = Array('arr', BitVecSort(8), BitVecSort(32))
arr = Array('arr', BV8, BV32)   # arr is an array from 8-bits BitVector to 32-bits BitVector
A   = Array('A', IS, IS)        # A is an array from integer to integer

#### Store this declaration into `tab`
# Suppose A is an array then the constraints A[x] = x, Store(A, x, y) == A are satisfiable
# for an array that contains an index x that maps to x, and when x == y.
solve(A[x] == x, Store(A, x, y) == A)

# In the end, arr would be:
# Store(Store(Store(Store(arr, 0, 1), 1, 1), 2, 0), 3, 1337)
arr = Store(arr, BitVecVal(0, 8), BitVecVal(1, 32))
arr = Store(arr, BitVecVal(1, 8), BitVecVal(1, 32))
arr = Store(arr, BitVecVal(2, 8), BitVecVal(0, 32))
arr = Store(arr, BitVecVal(3, 8), BitVecVal(1337, 32))
idx = BitVec('idx', 8)

# These are equivalent
# solve(Select(arr, idx) == 1337)
print("Which idx has value of 1337?")
solve(arr[idx] == 1337)

#### Constant arrays
# The arrays that maps to some fixed value can be specified using K(s, V) construct where
# s is the sort/type and v is the expression.
# K(s, v) returns an array that maps any value of s into v.
AllOne = K(IntSort(), 1)
a, i   = Ints('a i')
solve(a == AllOne[i])           # Have solution
solve(a == AllOne[i], a != 1)   # Doesn't have solution