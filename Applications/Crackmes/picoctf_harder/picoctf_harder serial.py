from z3 import *

solver = Solver()

serial = [ BitVec('serial_%d' % i, 32) for i in range(20) ]

# Only numbers allowed
for i in range(20):
    solver.add( 0 <= serial[i], serial[i] <= 9 )

solver.add( serial[15] + serial[4] == 10  )
solver.add( serial[1] * serial[18] == 2   )
solver.add( serial[15] / serial[9] == 1   )
solver.add( serial[17] - serial[0] == 4   )
solver.add( serial[5] - serial[17] == -1  )
solver.add( serial[15] - serial[1] == 5   )
solver.add( serial[1] * serial[10] == 18  )
solver.add( serial[8] + serial[13] == 14  )
solver.add( serial[18] * serial[8] == 5   )
solver.add( serial[4] * serial[11] == 0   )
solver.add( serial[8] + serial[9] == 12   )
solver.add( serial[12] - serial[19] == 1  )
solver.add( serial[9] % serial[17] == 7   )
solver.add( serial[14] * serial[16] == 40 )
solver.add( serial[7] - serial[4] == 1    )
solver.add( serial[6] + serial[0] == 6    )
solver.add( serial[2] - serial[16] == 0   )
solver.add( serial[4] - serial[6] == 1    )
solver.add( serial[0] % serial[5] == 4    )
solver.add( serial[5] * serial[11] == 0   )
solver.add( serial[10] % serial[15] == 2  )
solver.add( serial[11] / serial[3] == 0   )
solver.add( serial[14] - serial[13] == -4 )
solver.add( serial[18] + serial[19] == 3  )

solver.add( serial[3] != 0 )

while solver.check() == sat:
    print("Solution")
    model = solver.model()
    serial_s = [ chr(model[serial[i]].as_long() + ord('0')) for i in range(20) ]
    print("".join(serial_s))

    block = []
    for el in model:
        obj = el()
        block.append(obj != model[el])
    solver.add(Or(block))