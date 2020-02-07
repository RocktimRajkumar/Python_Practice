# Write a binary search function which searches an item in a sorted list. The function
# should return the index of element to be searched in the list.


def binary_search(a, l, r, val):

    if l <= r:
        mid = l+(r-l)//2

        if a[mid] == val:
            return mid

        if val > a[mid]:
            return binary_search(a, mid+1, r, val)

        else:
            return binary_search(a, l, mid-1, val)
    else:
        return 'Value Not Found'


len = int(input('Enter the number of elements '))
arr = []
for i in range(0, len):
    arr.append(int(input()))

arr.sort()

val = int(input('Enter the value to search '))
print(binary_search(arr, 0, len-1, val))
