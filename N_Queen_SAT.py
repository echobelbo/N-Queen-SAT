from z3 import *
# from datetime import datetime 
import time
n = int(input())


P = [[Bool("p_%s_%s" % (i + 1, j + 1)) for j in range (n)] for i in range (n)]
col_v = [Or([P[i][j] for i in range (n)]) for j in range (n)]
vol_v = [Or([P[i][j] for j in range (n)]) for i in range (n)]
col_d = [And([Or(Not(P[i][j]), Not(P[i][k])) for k in range (n) for j in range(k)]) for i in range (n)]
vol_d = [And([Or(Not(P[i][j]), Not(P[k][j])) for k in range (n) for i in range(k)]) for j in range (n)]
diag_d = [If((i + j == i_0 + j_0)or(i - j == i_0 - j_0) , Or(Not(P[i][j]), Not(P[i_0][j_0])), True) 
for i_0 in range (n) for i in range (i_0) for j_0 in range (n) for j in range (n)]
# start_ = datetime.utcnow() 
start_ = time.process_time()
solve(col_v + vol_v + col_d + vol_d + diag_d)
# end_ = datetime.utcnow() 
end_ = time.process_time()
c = (end_ - start_)

print(c, "miroseconds")