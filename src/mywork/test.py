from z3 import *
# template, set varaibles, add formulas, add everything to a solver, check the  solver's list, assign the variables using models
x = Bool('x')
y = Bool('y')
z = Bool('z')

f1 = Or(x,y,z)
f2 = Or(Not(x), Not(y))
f3 = Or(Not(y), Not(z))

F = And(f1, f2, f3)

s = Solver()
s.add(F)
print(s.check()) # Checks whats in the solver

m = s.model()

print(m.evaluate(x))
print(m.evaluate(y))
print(m.evaluate(z))
