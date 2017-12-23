from z3 import *

# create cells
cells = [Int('el%d' % i) for i in range(19)]

s = Solver()

# Format XXXX-XXXX-XXXX-XXXX
#        0123456789012345678

# The value of each element
for i in range(15):
    if i % 5 == 4:
        s.add( cells[i] == -3 )
    else:
        s.add( 0 <= cells[i], cells[i] <= 9 )

# Constraint 2: The elements at 15-18 are bound to value 3 tod 8
for i in range(15, 19):
    s.add( 3 <= cells[i], cells[i] < 8 )


sum_1st = cells[0] + cells[1] + cells[2] + cells[3]
sum_2nd = cells[5] + cells[6] + cells[7] + cells[8]
sum_3rd = cells[10]+ cells[11]+ cells[12]+ cells[13]
sum_4th = cells[15]+ cells[16]+ cells[17]+ cells[18]

avg_sum = (sum_1st + sum_2nd + sum_3rd)/3

# Constraint 3.1
s.add( sum_4th == avg_sum )

# Constraint 3.2
s.add( sum_1st == sum_4th / 4 )

# Constraint 4
s.add( sum_1st != sum_2nd )

# Constraint 5 and 6
for i in range(4):
    # Constraint 5: first[i]  != fourth[i]
    s.add( cells[i]   != cells[15+i] )
    # Constraint 6: second[i] != third[i]
    s.add( cells[5+i] != cells[10+i] )

count = 0
while s.check() == sat and count < 10:
    m = s.model()

    serial = []
    for i in range(19):
        serial.append(m[cells[i]].as_long() + 48)
    print("".join(map(lambda c: chr(c), serial)))

    block = []
    for el in m:
        obj = el()
        block.append(obj != m[el])
    s.add(Or(block))
    count += 1
