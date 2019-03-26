import numpy
a = [1,2,3,4]
b = [10,11,12,13]
print(a+b)
output = []
for item1, item2 in zip(a,b):
    output.append(item1+item2)


output




coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]
result = zip(coordinate, value)
resultList = list(result)
print(resultList)
c = zip(*resultList)
print('c =', c)