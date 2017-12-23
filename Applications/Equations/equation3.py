from z3 import *

dog, cat, mouse = Ints('dog cat mouse')

s = Solver()
s.add(dog >= 1, cat >= 1, mouse >= 1)
s.add(dog + cat + mouse == 100)
s.add(25*mouse + 100*cat + 1500*dog == 10000)

if s.check() == sat:
    m = s.model()
    print(m)
else:
    print("Not satisfied")