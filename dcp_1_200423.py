#!/usr/bin/python3
""" Daily Coding Problem #1 - 4/23/2020 """


def add_true_false(list=[], num=None):
    """
    Find if any two numbers from a given list
        adds up to the given number.
    Args:
        list: list of numbers
        num: number to match to
    Return:
        True: if two numbers adds up to num
        False: if no two numbers adds up to num
    """

    """
    Declare and initialize variables at the start
    and end of list
    """
    size = len(list)
    elmt_start = 0
    elmt_end = size - 1

    """
    Iterate through the list and compare the starting
    element to the ending element
    """
    for elmt_start in list:
        for elmt_end in list:
            if elmt_start + elmt_end == num:
                return True
    return False


""" Driver program for testing """
list = [10, 15, 3, 7]
num = 17
if add_true_false(list, num):
    print("Two numbers found that adds up to num")
else:
    print("No two numbers adds up to num")
