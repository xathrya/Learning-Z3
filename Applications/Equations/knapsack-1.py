# Solving knapsack problem with Z3
#
# Use: 
#    python knapsack.py 
#
from z3 import *

# from https://www.xkcd.com/287/ 

fruits, fries, salad, wings, sticks, plate = Ints('fruits fries salad wings sticks plate')

s = Solver()

s.add(fruits>=0,       fries>=0,   salad>=0,   wings>=0,   sticks>=0,   plate>=0)
s.add(215*fruits + 275*fries + 225*salad + 355*wings + 420*sticks + 580*plate == 1505)

result = []
while s.check() == sat:
    m = s.model()
    print(m)
    result.append(m)
    
    # Create new constraint the blocks the current model
    block = []
    for el in m:
        # el is a declaration
        if el.arity() > 0:
            raise Z3Exception("uninterpreted function are not supported")
        
        # Create a constant from declaration
        obj = el() 

        if is_array(obj) or obj.sort().kind() == Z3_UNINTERPRETED_SORT:
            raise Z3Exception("arrays and uninterpreted sorts are not supported")
        
        block.append(obj != m[el])
    
    s.add(Or(block))

print(len(result))

# https://stackoverflow.com/questions/141779/solving-the-np-complete-proble