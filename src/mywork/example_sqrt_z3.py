from z3 import *

def sqrt(n) :
    sqrtn = Real('sqrtn')
    s = Solver()
    s.add(sqrtn * sqrtn == n) # replace True with required declarative spec
    isSat = s.check()
    if (isSat == sat) :
        return s.model()
    return -1

def neg_sqrt(n) :
    sqrtn = Real('sqrtn')
    s = Solver()
    s.add(And(sqrtn * sqrtn == n, sqrtn < 0)) # replace True with required declarative spec
    isSat = s.check()
    if (isSat == sat) :
        return s.model()
    return -1
    

print(sqrt(9))
print(sqrt(100))
print(sqrt(24))

print(neg_sqrt(9))
print(neg_sqrt(100))
print(neg_sqrt(0))
