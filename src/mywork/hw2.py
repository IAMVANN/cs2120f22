from z3 import *
def p1():
    x, y, z = Bools('x y z')

    #X ∨ Y, X ⊢ ¬Y   
    #As Proposition:(x \/ y) /\ x -> !y X and 
    s = Solver()
    C1 = Implies(And(Or(x, y), x), Not(y))

    s.add(Not(C1))
    #I believe it is not valid
    s.check()
    #if the negation of the proposition is unsat, then the prop is valid
    if(s.check() == unsat):
        print("C1 is Valid")
    else : # otherwise we check if the model for the negation has any intrepretations that makes it true
        print("Here is a counter example : ", s.model())
def p2():
    
p1()
s.reset
p2()

