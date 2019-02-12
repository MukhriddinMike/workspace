import math

x, y = 5,10
f = 4.45645
stR = 'mike'
# print(math.copysign(y,x))
# print(math.frexp(x))
# print(math.isfinite(stR))
# print(math.isinf(10/3))
# print(math.ldexp(5))
print(math.trunc(f))
print(math.erf(x))

"""
def twice(x):
    return x*2


print(list(map(twice,([11,22,33,44]))))
"""

def foo(x1,x2):
    if x2 is None:
        return x1
    elif x1 is None:
        return x2
    else:
        return x1+x2


print(list(map(foo,[1,2],[10,20,30])))

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))
