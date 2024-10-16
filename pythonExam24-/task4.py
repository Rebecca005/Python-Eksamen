import random

numbers = [random.randint(1, 50) for _ in range(10)]


def substitute(lst):
    return [num**2 if num % 5 == 0 else num for num in lst]


print("Original list before substitution:", numbers)
numbers = substitute(numbers)
print("List after substitution:", numbers)
