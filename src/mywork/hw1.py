# Ivan Zheng uup2rt@virgina.edu
from itertools import combinations
from z3 import * 
# 5-queens solver
# Constraints
# - place 5 queens
# -  no 2 queens on the same row
# - no 2 queens are on the same colummn
# - No 2 queens on the same diagonal

def at_most_one(literals):
    c = []
    for pair in combinations(literals, 2):
        a, b = pair[0], pair[1]
        c += [Or(Not(a), Not(b))]
    return And(c)

# All the literals
x = [[Bool("x_%i_%i" % (i,j)) for j in range(5)] for i in range(5)]

s = Solver()
# Atleast 1 queens per row
for i in range(5): 
    s.add(Or(x[i]))
    
#Atmost 1 queen per colummn and atmost 1 queen per row
for i in range(5):
    col = []
    for j in range(5):
        col += [x[j][i]]
    s.add(at_most_one(col))
    s.add(at_most_one(x[i]))
        
#Atmost 1 queen per diagonal
for i in range(4):
    diag_1 = []
    diag_2 = [] 
    diag_3 = []
    diag_4 = []
    for j in range(5-i):
        diag_1 += [x[i+j][j]]
        diag_2 += [x[4-(i+j)][j]]
        diag_3 += [x[4-(i+j)][4-j]]
        diag_4 += [x[i+j][4-j]]
    s.add(at_most_one(diag_1))
    s.add(at_most_one(diag_2))
    s.add(at_most_one(diag_3))
    s.add(at_most_one(diag_4))
    
print(s.check())
m = s.model()

for i in range(5):
    line = ""
    for j in range(5): 
        if m.evaluate(x[i][j]):
            line += "x "
        else: 
            line += ". "
    print(line)    