"""Parse a python expression from a string and evaluate with a list of values.
"""

import parser
import random
import time


verbose = False
number_of_vars = 100000
max = 100000
var1_list = [max * random.random() for _ in range(number_of_vars)]
var2_list = [max * random.random() for _ in range(number_of_vars)]
var3_list = [max * random.random() for _ in range(number_of_vars)]

eq = "(var1 + var2) / var3 + 0.5"
code = parser.expr(eq).compile()

# To get variable names from equation:
# var_names = code.co_names

start = time.time()

for var1, var2, var3 in zip(var1_list, var2_list, var3_list):
    result = eval(code)
    if verbose:
        print '({var1} + {var2}) / {var3} ='.format(var1=var1, var2=var2, var3=var3), result

end = time.time()
print 'Performed {} evals in {} seconds ({} ops/sec)'.format(number_of_vars, end-start, number_of_vars / (end-start))
