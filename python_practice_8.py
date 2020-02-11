# Write a program which can map() to make a list whose elements are square of numbers
# between 1 and 20 (both included).
# Hints:
# Use map() to generate a list.
# Use Lambda to define anonymous functions.

result = map(lambda x: x*x, range(1,20+1))
print(list(result))