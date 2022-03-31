from z3 import *
# from datetime import datetime 

a_n = int(input("input the number of digits of your number in binary"))


a = input("input a in binary(low bit is in the front)")
b = input("input b in binary(low bit is in the front)")
a = a + '0'
b = b + '0'

A = [ Bool("a_%i" % i) for i in range (a_n + 1) ]
B = [ Bool("b_%i" % i) for i in range (a_n + 1) ]

A_t = [If(a[i] == '0', Not(A[i]),  A[i]) for i in range (a_n + 1)]
B_t = [If(b[i] == '0', Not(B[i]),  B[i]) for i in range (a_n + 1)]


C = [ Bool("c_%i" % i) for i in range (a_n + 1)]
D = [ Bool("d_%i" % i) for i in range (a_n + 1)]

Minus = [A[i] == (D[i] == (B[i] == C[i])) for i in range (a_n + 1)]
Minus_c = [C[i+1] == (Or(And(D[i], B[i]), And(D[i], C[i]), And(B[i], C[i]))) for i in range (a_n)]

solve(A_t + B_t + Minus + Minus_c + [Not(C[0])])