from z3 import *

# SEND + MORE = MONEY


D, E, M, N, O, R, S, Y = Ints('D E M N O R S Y')

solver = Solver()

solver.add(Distinct(D,E,M,N,O,R,S,Y))
solver.add(And(D>=0, D<=9)) 
solver.add(And(E>=0, E<=9)) 
solver.add(And(M>=0, M<=9)) 
solver.add(And(N>=0, N<=9)) 
solver.add(And(O>=0, O<=9)) 
solver.add(And(R>=0, R<=9)) 
solver.add(And(S>=0, S<=9)) 
solver.add(And(Y>=0, Y<=9)) 

solver.add( 1000*S + 100*E + 10*N + D + 1000*M + 100*O + 10*R + E == 1000*M + 1000*O + 100*N + 10*E + Y )

if solver.check() == sat:
    model = solver.model()
    print("SEND  =   {} {} {} {}".format(model[S],model[E],model[N],model[D]))
    print("MORE  =   {} {} {} {}".format(model[M],model[O],model[R],model[E]))
    print("------------------")
    print("MONEY = {} {} {} {} {}".format(model[M],model[O],model[N],model[E],model[Y]))