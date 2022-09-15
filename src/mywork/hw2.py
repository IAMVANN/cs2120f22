from z3 import *
def p1():
    x, y, z = Bools('x y z')

    #X ∨ Y, X ⊢ ¬Y   
    
    #As Proposition:(x \/ y) /\ x -> !y 
    
    s = Solver()
    C1 = Implies(And(Or(x, y), x), Not(y))
    # If (X Or Y) and X is true, then y has to be false

    s.add(Not(C1))
    #I believe it is not valid since if Y is true, the first half of the proposition
    # could be true(under the intrepretation that x is true), and then Y cannot be equal to false as it is true
    s.check()
    #if the negation of the proposition is unsat, then the prop is valid
    if(s.check() == unsat):
        print("C1 is Valid")
    else : # otherwise we check if the model for the negation has any intrepretations that makes it true
        print("C1 is not Valid. Here is a counter example : ", s.model())
        #This does not make sense because if both X and Y is true, then 
        #Y cannot be false as we just said it is true. 
def p2():
    #X, Y ⊢ X ∧ Y  
    x, y = Bools('x, y')
    
    # X /\ Y -> X/\Y
    s = Solver()
    C2 = Implies(And(x,y), And(x, y))
    #If both X and Y are true, then X AND Y has to be true
    
    # I believe this to be valid since its literally the same proposititon
    # character for character after you factor in the conjunction of the first half of the proposition.
    s.add(Not(C2))
    s.check()
    if(s.check() == unsat):
        print("C2 is Valid")
def p3():
    #X ∧ Y ⊢ X  
    # X /\ Y -> X
    x, y = Bools('x, y')
    s = Solver()
    C3 = Implies(And(x, y), x)
    #If X AND Y is true, then x has to be true
    
    #I believe this to be valid since in order for X AND Y to be true
    #both variables X and Y has to be true, and therefore x has to be true
    s.add(Not(C3))
    s.check()
    if(s.check() == unsat):
        print("C3 is valid")
    
def p4():
    #X ∧ Y ⊢ Y 
    #X/\Y ->Y
    x, y = Bools('x, y')
    s = Solver()
    C4 = Implies(And(x, y), y)
    #If X AND Y is true, then y has to be true
    
    #I believe this to be valid since in order for X AND Y to be true
    #both variables X and Y has to be equal to true, a nd therefore y has to be true
    s.add(Not(C4))
    s.check()
    if(s.check() == unsat):
        print("C4 is valid")
        
def p5():
    #¬¬X ⊢ X                   -- negation elimination 
    
    x = Bool('x')
    s = Solver()
    C5 = Implies(Not(Not(x)), x)
    #The opposite of the opposite of x is equal to x
    #I believe this to be valid since the negatives cancel each other out
    s.add(Not(C5))
    s.check()
    if(s.check() == unsat):
        print("C5 is valid")
        
def p6():
    #¬(X ∧ ¬X)                 -- no contradiction
    
    x = Bool('x')
    s = Solver()
    C6 = Not(And(x, Not(x)))
    #X cannot be X and Not(X) 
    
    #I believe this to be valid as X cannot be true and false at the same time
            
    s.add(Not(C6))
    s.check()
    if(s.check() == unsat):
        print("C6 is Valid")

def p7():
    #7. X ⊢ X ∨ Y                 -- or introduction left
    # X => X \/Y
    x, y = Bools('x, y')
    s = Solver()
    C7 = Implies(x, Or(x, y))
    #If X is true, then X Or Y has to be true
    
    # I believe this to be valid, for X or Y to be true, one of them has to be true
    #and in this case, one of them(x) will be true
    
    s.add(Not((C7)))
    s.check()
    if(s.check() == unsat):
        print("C7 is valid")
        
def p8():
    #8. Y ⊢ X ∨ Y                 -- or introduction right
    # Y => X \/
    x, y = Bools('x, y')
    s = Solver()
    C8 = Implies(y, Or(x, y))
    #If Y is True, then X Or Y has to be true
    
    #I believe this to be valid, for X or Y to be true, one of them has to be true
    # and in this case, one of them(y) will true
    
    s.add(Not(C8))
    s.check()
    if(s.check() == unsat):
        print("C8 is valid")
def p9():
    #9. X → Y, ¬X ⊢ ¬ Y           -- denying the antecedent
    # (X -> Y) /\ -x -> -y
    
    x, y = Bools()

p1()
p2()
p3()
p4()
p5()
p6()
p7()
p8()