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
    
    x, y = Bools('x, y')
    s = Solver()
    C9 = Implies(And(Implies(x, y), Not(x)), Not(y))
    #If X implies Y, And X is false, then Y has to be false
    
    # I believe this to be valid(Ended up being incorrect x => y != x =y)
    
    s.add(Not(C9))
    s.check()
    if(s.check() == unsat):
        print("c9 is valid")
    else : 
        print("C9 is not Valid. Here is a counter example : ", s.model())
        #Implications will result in a false if the first part of the implication is false, and the second is true
        #That interpretatuion can be used in this problem(on both sides), and so this equation cannot be valid as 
        #its possible to get false as a result 
def p10():
    #10. X → Y, Y → X ⊢ X ↔ Y      -- iff introduction
    # ((X -> Y) /\ Y->X) -> X == Y
    x, y = Bools('x, y')
    
    s = Solver()
    C10 = Implies(And(Implies(x,y), Implies(y, x)), And(Implies(x, y), Implies(y, x)))
    #If whenever X is true, Y has to be true, and whenever Y is true, X has to be true
    # then X is equal to Y
    
    s.add(Not(C10))
    s.check()
    #I think this is valid because both X and Y will be equal to true thus equal to each other
    if(s.check() == unsat):
        print("C10 is valid")
        
def p11():
    #11. X ↔ Y ⊢ X → Y            -- iff elimination left
    x, y = Bools('x, y')
    s = Solver()
    C11 = Implies(And(Implies(x, y), Implies(y, x)), Implies(x, y))
    #If whenever X is true, y must be true, and whenever y is true, x has to be true
    #then, whenever x is true, then y must be true as well
    s.add(Not(C11))
    s.check()
    #I think this is valid since part of the original statement address X -> Y
    if(s.check() == unsat):
        print("C11 is valid")
def p12():
    #12. X ↔ Y ⊢ Y → X            -- iff elimination right
    # (X -> Y /\ Y -> x) -> (y->x)
    x, y = Bools('x, y')
    s = Solver()
    C12 = Implies(And(Implies(x, y), Implies(y, x)), Implies(y, x))
    #If whenever X is true, y must be true, and whenever y is true, x has to be true
    #then, whenever y is true, then x must be true as well
    s.add(Not(C12))
    s.check()
    #I think this is valid since the original statement addresses y->x 
    if(s.check() == unsat):
        print("C12 is valid")
def p13(): 
    #13. X ∨ Y, X → Z, Y → Z ⊢ Z  -- or elimination
    # ((X \/ Y) /\ (X -> Z) /\ (Y->Z)) -> Z
    x, y, z = Bools('x, y, z')
    s = Solver()
    C13 = Implies(And(And(Or(x, y), Implies(x, z)), Implies(y, z)),z)
    # If (X or Y) and whenever x is true, Z is true and whenever y is true, Z is true, is true, 
    # then Z must be true as well. 
    
    s.add(Not(C13))
    s.check()
    #I think this is valid, since Z has to be true whenever the thing implying it is true
    #and we are garuanteed that one of those is true with the or statement infront
    if(s.check() == unsat):
        print("C13 is valid")
def p14():
    #14. X → Y, Y ⊢ X             -- affirming the conclusion
    # (X->Y)/\ Y --> 
    x, y = Bools('x, y')
    s = Solver()
    C14 = Implies(And(Implies(x, y), y), x)
    #Whenever x is true, then y has to be true AND y is true, sp x must be true
    
    s.add(Not(C14))
    s.check()
    
    #I think this is invalid since x being true or not does not depend on y
    if(s.check() == unsat):
        print("C14 is valid")
    else : 
        print("C14 is not Valid. Here is a counter example : ", s.model())
        #X being true or not does not depend on y in this  proposition, so it would be possible for the prior part of the proposition
        #to be true, while x is false, making this proposition not valid

def p15():
    #15. X → Y, X ⊢ Y             -- arrow elimination
    #(X -> Y) /\ X, -> Y
    x, y = Bools('x, y')
    s = Solver()
    C15 = Implies(And(Implies(x, y), x), y)
        #Whenever x is true, then y has to be true AND x is true, then Y has to be true
    s.add(Not(C15))
    s.check()
    
    #I think this is valid because whenever x is true, y has to be true. And we established the fact that x is true, so y is true
    
    if(s.check() == unsat):
        print("C15 is valid")
def p16():
    #16. X → Y, Y → Z ⊢ X → Z     -- transitivity of → 
    # ((X -> Y) /\ (Y -> Z)) -> (x->z)
    x, y, z = Bools('x, y, z')
    s = Solver()
    C16 = Implies(And(Implies(x, y), Implies(y, z)), Implies(x, z))
    #If whenever x is true, y is true, And whenever Y is true, then Z is true, then whenever x is true, Z is true
    s.add(Not(C16))
    s.check()
    
    #I think this is valid 
    if(s.check() == unsat):
        print("C16 is valid")
def p17():
    #17. X → Y ⊢ Y → X            -- converse
    # (x -> y) -> (Y -> X)
    x, y = Bools('x, y')
    s = Solver()
    C17 = Implies(Implies(x, y), Implies(y, x))
    #If whenever x is true, y is true, then whenver y is true, x has to be true
    s.add(Not(C17))
    s.check()
    
    #I think this is valid
    if(s.check() == unsat):
        print("C17 is valid")
    else : 
        print("C17 is not Valid. Here is a counter example : ", s.model())
        #This is not valid since in the first part of the proposition, when x is false, y could be true.
        #When this intrepretation is taken to the second half of the proposition, Implies(y, x), that would evaulate as false
        # and since the first part of the proposition is true under this interepretaion and the second is false, this propostion is not valid
def p18():
    # X → Y ⊢ ¬Y → ¬X   
    # (X-> Y) -> (¬Y → ¬X)
    x,y = Bools('x, y')
    s = Solver()
    C18 = Implies(Implies(x, y), Implies(Not(y), Not(x)))
    #If whenever x is true, y is true, then whenever y is false, then x is false
    s.add(Not(C18))
    s.check()
    #I think this is valid
    if(s.check() == unsat): 
        print("C18 is valid")
def p19():
    # ¬(X ∨ Y) ↔ ¬X ∧ ¬Y 
    # (¬(X ∨ Y) -> ( ¬X ∧ ¬Y )) /\( ¬X ∧ ¬Y )) ->¬(X ∨ Y))
    x, y = Bools('x, y')
    s = Solver()
    C19 = And(Implies(Not(Or(x, y)), And(Not(x), Not(y))),Implies(And(Not(x), Not(y)),Not(Or(x, y))))
    #The opposite of (X Or Y) is Not X and Not Y
    s.add(Not(C19))
    #I think this is valid
    s.check()
    if(s.check()== unsat): 
        print("C19 is valid")
def p20():
    #20. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y  
    #(¬(X ∧ Y) -> ¬X ∨ ¬Y  ) /\ (¬X ∨ ¬Y ->¬(X ∧ Y) )
    x, y = Bools('x, y')
    s = Solver()
    C20 = And(Implies(Not(And(x, y)), Or(Not(x), Not(y))), Implies( Or(Not(x), Not(y)),Not(And(x, y)), ))
    #The opposite of (X and Y) is Not X or Not y
    s.add(Not(C20))
    #I think this is valid
    s.check()
    if(s.check()== unsat): 
        print("C20 is valid")
p1()
p2()
p3()
p4()
p5()
p6()
p7()
p8()
p9()
p10()
p11()
p12()
p13()
p14()
p15()
p16()
p17()
p18()
p19()
p20()