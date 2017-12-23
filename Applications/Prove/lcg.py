from z3 import *

# Prove
# There are well known weakness of LCD [1], but can it be crack straightforwardly,
# without any special knowledge

# suppose following code in C 
#    int i;
#    srand(time(NULL));
#    for (i=0; i<10; i++) printf("%d\n", rand()%100);
#
# yields following output 
#    37, 29, 74, 95, 98, 40, 23, 58, 61, 17
#
# Let's say we observe 8 numbers (from 29 to 61) and we need to predict the 
# next one (17) or the previous one (37).
# and the LCG used is:
#    .text:0040112E rand proc near
#    .text:0040112E call __getptd
#    .text:00401133 imul ecx, [eax+0x14], 214013
#    .text:0040113A add ecx, 2531011
#    .text:00401140 mov [eax+14h], ecx
#    .text:00401143 shr ecx, 16
#    .text:00401146 and ecx, 7FFFh
#    .text:0040114C mov eax, ecx
#    .text:0040114E retn
#    .text:0040114E rand endp

# Declare variables
output_prev = BitVec('output_prev', 32)
state1 = BitVec('state1', 32)
state2 = BitVec('state2', 32)
state3 = BitVec('state3', 32)
state4 = BitVec('state4', 32)
state5 = BitVec('state5', 32)
state6 = BitVec('state6', 32)
state7 = BitVec('state7', 32)
state8 = BitVec('state8', 32)
state9 = BitVec('state9', 32)
state10 = BitVec('state10', 32)
output_next = BitVec('output_next', 32)

s = Solver()

# Constraint of LCG
s.add(state2 == state1*214013+2531011)
s.add(state3 == state2*214013+2531011)
s.add(state4 == state3*214013+2531011)
s.add(state5 == state4*214013+2531011)
s.add(state6 == state5*214013+2531011)
s.add(state7 == state6*214013+2531011)
s.add(state8 == state7*214013+2531011)
s.add(state9 == state8*214013+2531011)
s.add(state10 == state9*214013+2531011)

s.add(output_prev==URem((state1>>16)&0x7FFF,100))
s.add(URem((state2>>16)&0x7FFF,100)==29)
s.add(URem((state3>>16)&0x7FFF,100)==74)
s.add(URem((state4>>16)&0x7FFF,100)==95)
s.add(URem((state5>>16)&0x7FFF,100)==98)
s.add(URem((state6>>16)&0x7FFF,100)==40)
s.add(URem((state7>>16)&0x7FFF,100)==23)
s.add(URem((state8>>16)&0x7FFF,100)==58)
s.add(URem((state9>>16)&0x7FFF,100)==61)
s.add(output_next==URem((state10>>16)&0x7FFF,100))

print(s.check())
print(s.model())


# [1] http://en.wikipedia.org/wiki/Linear_congruential_generator#Advantages_and_disadvantages_of_LCGs
#     http://www.reteam.org/papers/e59.pdf
#     http://stackoverflow.com/questions/8569113/why-1103515245-is-used-in-rand/8574774#8574774