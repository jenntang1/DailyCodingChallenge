#!/usr/bin/python3
""" Daily Coding Problem #4 - 4/27/2020 """


def cons(a, b):
    """
    Constructs a pair of integers
    Note:
        Inspired by https://stackoverflow.com/questions/
        52481607/dont-understand-the-inner-function-in-
        python
    Args:
        a: first integer in pair
        b: second integer in pair
    Return:
        a pair
    """
    def pair(f):
        """
        Function created by def cons(a, b) that
        inherits a and b
        """
        return f(a, b)
    return pair


def car(f):
    """ Returns first integer in a pair """
    def first(a, b):
        """ Function calls def pair(f) """
        return a
    return f(first)


def cdr(f):
    """ Returns second integer in a pair """
    def second(a, b):
        """ Function calls def pair(f) """
        return b
    return f(second)


""" Driver program for testing """
pair = cons(3, 4)
print("First of a pair: {}".format(car(pair)))
print("Second of a pair: {}".format(cdr(pair)))
