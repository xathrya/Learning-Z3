from z3 import *

# H+E+L+L+O = W+O+R+L+D = 25

D, E, H, L, O, R, W = Ints('D E H L O R W')

solver = Solver()

solver.add(Distinct(D, E, H, L, O, R, W,))
solver.add(And(D>=0, D<=9)) 
solver.add(And(E>=0, E<=9)) 
solver.add(And(H>=0, H<=9)) 
solver.add(And(L>=0, L<=9)) 
solver.add(And(O>=0, O<=9)) 
solver.add(And(R>=0, R<=9)) 
solver.add(And(W>=0, W<=9))

solver.add(H+E+L+L+O == W+O+R+L+D, W+O+R+L+D == 25)

if solver.check() == sat:
    model = solver.model()
    print("HELLO  =  {} {} {} {} {}".format(model[H],model[E],model[L],model[L],model[O]))
    print("WORLD  =  {} {} {} {} {}".format(model[W],model[O],model[R],model[L],model[D]))