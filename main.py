# numbers = [1, 2, 3, 4, 5, 6, 7]

# result = []
#
# for item in numbers:
#     result.append(item ** item)
#
# print(result)

# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

import sys

numbers = [i ** 2 for i in range(10000000)]
print(sys.getsizeof(numbers))

def square_number():
    for num in numbers:
        yield num ** 2

print(sys.getsizeof(square_number()))