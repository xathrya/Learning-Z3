# Solving liar paradox usign Z3
#
# Use: 
#    python liar-paradox.py 
# 
from z3 import *

solver = Solver()


# Declare some type
Nationalities, (Cretans, EveryoneElse) = EnumSort('Nationalities', ('Cretans', 'EveryoneElse'))
Honesty, (Liar, Honest) = EnumSort('Honesty', ('Liar','Honest'))

speaker = Const('speaker', Honesty)
nationality = Const('nationality', Nationalities)

# All cretans are liars.
statement = And(
    Implies(nationality == Cretans, speaker == Liar),
    Implies(speaker == Liar, False)
)
paradox = nationality == Cretans 

solver.add(statement, paradox)

if solver.check() == sat:
    model = solver.model()

    print("SAT!")
    print("Speaker: {}\tNationality: {}\n".format(model[''], model['']))
else:
    print('UNSAT!')