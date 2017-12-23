# ganben
# question source: http://philosophy.hku.hk/think/logic/knights.php  Hongkong University
from z3 import *

# A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.

# Q1

# You meet two inhabitants: Zoey and Mel.
# Zoey tells you that Mel is a knave.
#
# Mel says, “Neither Zoey nor I are knaves.”
# var declare
kt, kv= Ints('kt kv')
zoey, mel = Ints('zoey mel')
#check if zoey == 1 == kt;
s = Solver()
#s0.add(Distinct(zoey, mel))
#constrains 1, or 2 1 == kt, 2 == kv
s.add(zoey>=1, zoey<=2)
s.add(mel>=1,  mel<=2)
#add assume:
s.add(zoey == 1, mel == 2)
#add sayings
s.add(mel==2)
s.add(Xor(mel != 2, zoey != 2)) #negation due to 2
r = s.check()

if r == unsat:
    print('Q1: zoey mel <> 1 2')

else:
    print('Q1: zoey = 1, mel = 2')
    print(s.model())

#assume 2: zoey == 2 == kv
s = Solver()
#s1.add(Distinct(zoey, mel))
#constrains 1, or 2 1 == kt, 2 == kv
s.add(zoey>=1, zoey<=2)
s.add(mel>=1,  mel<=2)
#add assumes
s.add(zoey ==2, mel ==1)
#add sayings
s.add(mel != 2) # negation due to 2
s.add(mel != 2, zoey != 2)
r = s.check()
if r == unsat:
    print('Q1: zoey mel <> 2 1')
else:
    print(s.model())


#Q2
# Peggy tells you that “of Zippy and I, exactly one is a knight'.
# Zippy tells you that only a knave would say that Peggy is a knave.
peggy, zippy = Ints('peggy zippy')

s = Solver()
s.add(zoey>=1, zoey<=2)
s.add(mel>=1,  mel<=2)

#cases: p, z = [1 1] [1 2] [2 1] [2 2]

#cases p, z = [1 2] or [2 1]
#s.add(Distinct(peggy, zippy))
s.add(Or((peggy == 1 and zippy == 2), (peggy == 2 and zippy == 2)))
s.add(Or((peggy == 2 and zippy == 2), (peggy == 1 and zippy == 1)))
r = s.check()
if r == unsat:
    print('Q2: ??')
else:
    print(s.model())