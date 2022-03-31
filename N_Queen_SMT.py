from z3 import *
# from datetime import datetime 
import time

n = int(input())

# print(n)
Q = [ Int('Q_%s' % (i + 1)) for i in range(n) ]
val_c = [ And(1 <= Q[i], Q[i] <= n) for i in range(n) ]
col_c = [ Distinct(Q) ]
diag_c = [ If(i == j, True, And(i + Q[i] != j + Q[j], i + Q[j] != j + Q[i])) for i in range(n) for j in range(i) ]
# start_ = datetime.utcnow() 
start_ = time.process_time()
solve(val_c + col_c + diag_c)
# end_ = datetime.utcnow() 
end_ =time.process_time()
c = (end_ - start_)
print(c, "miroseconds")
# n = input()
