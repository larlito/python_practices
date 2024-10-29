#1
from functools import reduce

array =  ['1','20','300']
new_array  = list(map(lambda x:int(x),array))
print(new_array)


#2

array = [1,2,3,4,5,6]
def func(x : int):
    if x % 2 == 0:
        return x
new_array = filter(func,array)
print(list(new_array))


#3

array = [1,2,3,4]
new_array = list(map(lambda x: x ** 2,array))
print(new_array)


#4
array = ["cat", "elephant", "dog", "tiger"]
new_array = filter(lambda x: len(x) > 3,array)
print(list(new_array))


#5
array = [1,2,3,4]
new_array = reduce(lambda a,b:a * b, array)
print(new_array)

#6
array = ["hello", "world", "Python"]
new_array = list(map(lambda x: len(x),array))
print(new_array)

#7
array = ["apple", "banana", "pear", "strawberry"]
result = len(reduce(lambda a,b: a if a > b else b,array))
print(result)

#8
array = ["hello", "world"]
new_array = list(map(lambda x:x.upper(),array))
print(new_array)


#9
array = ["1", "2", "3", "4"]
new_array = list(filter(lambda x: (int(x) % 2 == 0),array))
result = list(map(lambda x: int(x) ** 2,new_array))
print(result)

#10
array = [-2, 3, -4, 5, 6]
new_array = list(filter(lambda x: x > 0,array))
result = reduce(lambda a,b: a * b,new_array)
print(result)

