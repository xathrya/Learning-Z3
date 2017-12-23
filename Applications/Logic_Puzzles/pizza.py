from z3 import *

s = Solver()

# Baker make three pizzas, one at a time, each with two toppings
pizza = Function('pizza', IntSort(), IntSort(), IntSort())

# There are 6 toppings
anchovies, bacon, mushrooms, peppers, sausage, tomatoes = Ints('anchovies bacon mushrooms peppers sausage tomatoes')

for i in [anchovies, bacon, mushrooms, peppers, sausage, tomatoes]:
    s.add(0 <= i, i <= 5)

# No toppings can be put on more than one pizza 
s.add(Distinct(anchovies, bacon, mushrooms, peppers, sausage, tomatoes))

# C1: anchovies canot be paired with peppers
s.add(anchovies/2 != peppers/2)

# C2: mushrooms and tomatoes must be on the same pizza
s.add(mushrooms/2 == tomatoes/2)

# C3: Sausage must be on the second pizza if mushroom are on the first
s.add(Implies(mushrooms/2 == 0, Or(sausage == 2, sausage == 3)))

# C4: peppers must be made after the pizza with sausage
s.add(If(sausage%2 == 0, peppers == sausage == sausage + 2, peppers == sausage + 1))

while s.check() == sat:
    m = s.model()
    print(m)
    block = []
    for el in m:
        obj = el()
        block.append(obj != m[el])
    s.add(Or(block))