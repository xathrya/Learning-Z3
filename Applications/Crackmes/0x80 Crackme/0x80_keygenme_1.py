from z3 import *

# Format: WWWW-XXXX-YYYY-ZZZZ
serial =  [ BitVec('serial_%d' % i, 32) for i in range(19) ]

solver = Solver()

# Constraint
## Dash is in position 4, 9, 14
solver.add( serial[4] == ord('-'), serial[9] == ord('-'), serial[14] == ord('-') )

## Serial is all numbers
for i in range(19):
    if i in [4, 9,14]: # skip giving constraint to dash
        continue
    solver.add( ord('0') <= serial[i], serial[i] <= ord('9') )

## Each part has value of sum(part)/k
sums  = [ BitVec('sum_%d' % i, 32) for i in range(4) ]
parts = [ BitVec('part_%d' % i, 32) for i in range(4) ]

run_sum = 0
for i in range(4):
    run_sum = sums[i] + run_sum
    solver.add( sums[i] == serial[5*i] + serial[5*i + 1] + serial[5*i + 2] + serial[5*i + 3] )
    solver.add( parts[i] == run_sum/(i+1) )
    solver.add( parts[i] == ( sums[0] + sums[1] + sums[2] + sums[3])/4 )

## 
for i in range(4):
    solver.add( serial[i] != serial[i + 5], serial[i+5] != serial[i+10], serial[i+10] != serial[i+15] )

print("Searching the satisfying model...")

# Solve the constraint
while solver.check() == sat:
    model = solver.model()

    serial_int = [ chr(model[serial[i]].as_long()) for i in range(19) ]
    print("".join(serial_int))

    block = []
    for el in model:
        obj = el()
        block.append(obj != model[el])
    solver.add(Or(block))