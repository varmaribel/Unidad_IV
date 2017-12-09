"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

class Person:

    foo = 'bar'

    def __init__(self, first, last, age):
        self.first = first
        self.last  = last
        self.age = age
        

    def greet(self):
        return 'Hello there'


    @staticmethod
    def wave():
        return foo

    @classmethod
    def say_foo(cls):
        return cls.foo
