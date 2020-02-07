# Define a class Person and its two child classes: Male and Female. All classes have a
# method &quot;get_gender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
# Class.
# Bonus: Make class Person an abstract class and make get_gender an abstract method in the
# same class. The two child classes must inherit and implement get_gender. i.,e, When trying to
# initialize an object of class Person, the program must throw error.
# Hint:
# Use abc library (comes natively with Python3) https://www.python-
# course.eu/python3_abstract_classes.php

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_gender(self):
        pass


class Male(Person):
    def get_gender(self):
        print('Male')

class Female(Person):
    def get_gender(self):
        print('Female')

person = Female()
person.get_gender()