# N-Queen-SAT

三个部分

使用z3库解决了N皇后问题和一个减法的pure-SAT实现

N_Queen_SMT.py提供了N皇后问题的SMT解答办法并统计了运行时间

N_Queen_SAT.py提供了N皇后问题的pure-SAT解答办法并统计了运行时间

Minus_SAT.py提供了减法的pure-SAT实现（仅满足了对d=a-b中a，b都为正整数且a>b情况的支持）

Minus_SAT.py使用方式如下，首先输入a在二进制中的最高位数，然后低位在前依次输入a和b，输出结果中d对应的true值为1，false为0，输出结果