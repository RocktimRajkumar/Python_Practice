# Write an iterator class ReverseIter, that takes a list and iterates it from the reverse
# Direction.


class ReverseIter:

    def __init__(self, lst):
        self.a = lst

    def __iter__(self):
        self.len = len(self.a)-1
        return self

    def __next__(self):
        if self.len >= 0:
            x = self.a[self.len]
            self.len -= 1
            return x
        else:
            raise StopIteration


myrev = ReverseIter([1, 2, 3, 4, 5])
myiter = iter(myrev)

for x in myiter:
    print(x)
