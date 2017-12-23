# Solving coin-sum problem with Z3
#
# Use: 
#    python coin-sum.py 
# 

from z3 import *

p1,p2,p5,p10,p20,p50,l1,l2 = Ints('p1 p2 p5 p10 p20 p50 l1 l2')

s = Solver()

s.add(p1>=0,  p2>=0, p5>=0,  p10>=0,  p20>=0,  p50>=0,   l1>=0,   l2>=0)
s.add(p1 +  2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*l1 + 200*l2 == 200)

result = []
while s.check() == sat:
    m = s.model()
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