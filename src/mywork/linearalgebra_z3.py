from z3 import *
x = Real('X')
y = Real('Y')
z = Real('Z')
s = Solver()
s.add(3*x + 2*y -z == 1)
s.add(2*x + 2*y+4*z==-2)
s.add(-x+.5*y-z == 0)
if(s.check() == sat):
    m = s.model()
    print(m.evaluate(x))
    print(m.evaluate(y))
    print(m.evaluate(z))
    
else: 
    print("There is no solution")

