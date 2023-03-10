#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

resultadd = add(a, b)
resultsub = sub(a, b)
resultmul = mul(a, b)
resultdiv = div(a, b)

print("{} + {} = {}".format(a, b,resultadd))
print("{} - {} = {}".format(a, b,resultsub))
print("{} * {} = {}".format(a, b,resultmul))
print("{} / {} = {}".format(a, b,resultdiv))
