from z3 import *
from time import time

serial = [ BitVec('serial{}'.format(i), 32) for i in range(13) ]

solver = Solver()

# constraint 1
for i in range(13):
    solver.add(0 <= serial[i], serial[i] <= 9)

# constraint 2
total_expr = 3
for i in range(12):
    total_expr += 2 * total_expr ^ serial[i]

solver.add(serial[12] == total_expr % 10)

if solver.check() == sat:
    model = solver.model()
    print("".join([ chr(model[serial[i]].as_long() + ord('0')) for i in range(13) ]))
else:
    print("Not satisfied!")