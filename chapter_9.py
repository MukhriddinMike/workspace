import operator
'''
print(bin(60&30))
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer
def son(n=5):
    print("Hello" if n > 10 else "Goodbye" if n > 5 else "Good day")
son()
s1='Mike'
for count,ele in enumerate(s1,100):
    print (count,ele )
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)
    
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

#print(x)

#convert the map into a list, for readability:
print(list(x))
x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(list(x))

for i in range(3):
    print(i)
else:
    print('done')
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')


d = {"a": 1, "b": 2, "c": 3}
for value in d.values():
    print(value)
    #value example

# this is iteration with index umbers

lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

for idx,s in enumerate(lst):
    print("%s has an index of %d" % (s,idx))


for s in lst[1::2]:
    print(s)
    
   
import cmath
complex_num = cmath.sqrt(-1)
while complex_num: # You can also replace complex_num with any number, True or a value of any
    type
    print(complex_num) # Prints 1j forever




from array import *
my_array=array('i',[1,2,3,4,5])
my_sec_array=array('i',[7,8,9])
my_array.insert(0,0)
my_array.append(6)
my_array.extend(my_sec_array)
c=[11,12,13]
my_array.fromlist(c)


lst=[1,2,3,4]
b=[5,6,7]
lst.extend(b)
print(lst)
my_list=[{1} for _ in range(10)]
print(my_list)
str='Mike Wood'
squares=[x*x for x in b]
print(squares)

def squares(x):
    return x*x
m=map(squares, b)
print(list(m))

squares=[]
for x in b:
    squares.append(x*x)
print(squares)
mike_lambda=[]
x=lambda z:z*z
print(x(int(7)))


print()
print()

import heapq
num=[1,2,3,4,5,6,3,34,34,45,56,34,23,34532,23,344]
largest=heapq.nlargest(2,num)
print(largest)
smallest=heapq.heapify(4)
print(smallest)

'''
import heapq
people = [
{'firstname': 'John', 'lastname': 'Doe', 'age': 30},
{'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
{'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
{'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
{'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
{'firstname': 'John', 'lastname': 'Roe', 'age': 45}
]
oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
print(oldest)

num=[1,2,3,4,5,6,3,34,34,45,56,34,23,34532,23,344]

heapq.heappop(num) # 2
print(num)
heapq.heappop(num) # 2
print(num)
heapq.heappop(num) # 2
print(num)
heapq.heappop(num) # 2
print(num)
heapq.heappop(num) # 2
print(num)
heapq.heappop(num) # 2
print(num)
heapq.heappop(num) # 2
print(num)
heapq.heappop(num) # 2
print(num)
heapq.heappop(num) # 2
print(num)

import tuple
print()
tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
print(cmp(tuple1, tuple2))