#!/usr/bin/python3
""" Daily Coding Problem #5 - 5/1/2020 """


def max_sum(list=[]):
    """
    Find maximum sum of non-adjacent numbers
    Note:
        O(n) time complexity
    Args:
        list: list of numbers
    Return:
        maximum sum
    """

    """
    Declare and initializae variables for calculating
    maximum sum that includes the current element
    and another that excludes it
    """
    include = 0
    exclude = 0
    new = 0

    """
    Iterate through list and keep track of two sums:
    include (sums the previous element) and
    exclude (doesn't sum the previous element)
    """
    for element in list:
        if include > exclude:
            new = include
        else:
            new = exclude
        include = exclude + element
        exclude = new

    """
    Return the greater of the two sums tracked
    """
    if include > exclude:
        return include
    else:
        return exclude


""" Driver program for testing """
list_1 = [2, 4, 6, 2, 5]
list_2 = [5, 1, 1, 5]
print("Max sum in list_1 is {}".format(max_sum(list_1)))
print("Max sum in list_2 is {}".format(max_sum(list_2)))
