from z3 import *

# VIOLIN+VIOLIN+VIOLA = TRIO+SONATA

A, I, L, N, O, R, S, T, V = Ints('A I L N O R S T V')
VIOLIN, VIOLA, SONATA, TRIO = Ints('VIOLIN VIOLA SONATA TRIO')

solver = Solver()

solver.add(Distinct(A, I, L, N, O, R, S, T, V))
solver.add(And(A>=0, A<=9)) 
solver.add(And(I>=0, I<=9)) 
solver.add(And(L>=0, L<=9)) 
solver.add(And(N>=0, N<=9)) 
solver.add(And(O>=0, O<=9)) 
solver.add(And(R>=0, R<=9)) 
solver.add(And(S>=0, S<=9)) 
solver.add(And(T>=0, T<=9)) 
solver.add(And(V>=0, V<=9)) 

solver.add(VIOLIN == 100000*V + 10000*I + 1000*O + 100*L + 10*I + N)
solver.add(VIOLA  ==            10000*V + 1000*I + 100*O + 10*L + A)
solver.add(SONATA == 100000*S + 10000*O + 1000*N + 100*A + 10*T + A)
solver.add(TRIO   ==                      1000*T + 100*R + 10*I + O)
solver.add( VIOLIN + VIOLIN + VIOLA == TRIO + SONATA )

if solver.check() == sat:
    model = solver.model()
    print("VIOLIN  =   {}".format(model[VIOLIN]))
    print("MORE    =   {}".format(model[VIOLA]))
    print("------------------")
    print("TRIO    =   {}".format(model[TRIO]))
    print("SONATA  =   {}".format(model[SONATA]))