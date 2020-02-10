# Write a program using generator to print the numbers which can be divisible by 5
# and 7 between 0 and n in comma separated form while n is input by console.


def divisible(n):
    for i in range(0,n):
        if i%5==0 and i%7==0:
            yield i

n = int(input('Enter the value of n '))
res = divisible(n)

print(','.join(str(x) for x in res))