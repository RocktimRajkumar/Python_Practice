# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
# after removing all duplicate values with original order reserved.
# Hint: Use set() to store a number of values without duplicates.

lst = [12,24,35,24,88,120,155,88,120,155]

notDuplicate = list(set(lst))

def notInDuplicate(i):
    if i in notDuplicate:
        notDuplicate.remove(i)
        return True
    else:
        return False

res = list(filter(notInDuplicate,lst))


print(res)