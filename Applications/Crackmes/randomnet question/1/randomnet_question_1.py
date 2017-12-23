from z3 import *

"""
https://reverseengineering.stackexchange.com/questions/11303/how-to-break-this-reversing-exercise
"""

not_random = [18467, 6334, 26500, 19169, 15724, 11478, 29358, 26962, 24464, 5705, 28145, 23281, 16827, 9961, 491, 2995, 11942, 4827, 5436, 32391, 14604, 3902, 153, 292, 12382, 17421, 18716, 19718, 19895, 5447, 21726, 14771, 11538, 1869, 19912, 25667, 26299, 17035, 9894, 28703, 23811]
key = [ BitVec('key_%d' % i, 32) for i in range(5) ]

def solve_iterate(digit):
    # Declare
    globals()['key_%d' % digit] = BitVec('key_%d' % digit, 32)

    # Append
    key.append(globals()['key_%d' % digit])

    # Create solver
    solver = Solver()

    password = []
    for i in range(len(key)):
        solver.add( 0 <= key[i], key[i] <= 255 )
        password.append( key[i] ^ not_random[i] )

    sub_formula = 0x1337
    for i in range(len(key)-1, -1, -1):
        sub_formula = sub_formula * password[i] + 0x31337
        
    solver.add( sub_formula == 0xFD0970E7 )

    if solver.check() == sat:
        print(solver.model())
    else:
        print("No solution for this")


import IPython; IPython.embed()