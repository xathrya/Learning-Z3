from z3 import *
from functools import reduce

# Create serial numbers
serial = [ BitVec('serial{}'.format(i), 32) for i in range(10) ]

def check(digit):
    solver = Solver()

    serial.append( BitVec('serial{}'.format(digit-1), 32) )

    # Add constraints
    #### All digits must be within 0-9 inclusive
    for i in range(digit):
        solver.add(0 <= serial[i], serial[i] <= 9)
    
    #### There exists a digit 0
    block = []
    for i in range(len(serial)):
        block.append(serial[i] == 0)
    solver.add(Or(block))

    #### Sum of even pos digits + sum of odd pos digits * 3 % 10 == 1
    solver.add((
        reduce(lambda a,b: a + b, serial[0:-1:2])
         + 
        reduce(lambda a,b: a + b, serial[1:-1:2])*3 
        ) % 10 == 1 )

    #### Sum of first 5 digits should be equal 21
    solver.add( reduce(lambda a,b: a + b, serial[0:5]) == 21 )

    #### Product of 4 digits after the first one is 480
    solver.add( reduce(lambda a,b: a * b, serial[1:5]) == 480 )

    #### Digits from 5 to 10 should be 914323 (hardcoded value)
    solver.add(serial[5] == 9, serial[6] == 1, serial[7] == 4, serial[8] == 3, serial[9] == 2, serial[10] == 3)

    #### Constraint involving math abs
    solver.add(Or(serial[1] + serial[2] - serial[3] == 1, serial[1] + serial[2] - serial[3] == -1))
    solver.add(Or(serial[1] + serial[2] - serial[4] == 1, serial[1] + serial[2] - serial[4] == -1))

    #### Last digits must be 9
    solver.add(serial[digit-1] == 9)

    # Check if there is satisfying solution to the problem
    n = 0
    print("Checking for {} digits".format(digit))
    while solver.check() == sat:
        n += 1
        model = solver.model()
        print("Found passcode: " + reduce(lambda a, b: a + str(model[b]), ([''] + serial)))        
        
        block = []
        for el in model:
            obj = el()
            block.append(obj != model[el])
        solver.add( Or(block) )
    
    print("Serial check finished with {} match(es)!".format(n))
    return

for i in range(11,15):
    check(i)