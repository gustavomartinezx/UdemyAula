import sys

iterable = [3, 2, 1]
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))   

generator = (n for n in range(10))
print(sys.getsizeof(generator))