#!/usr/bin/python3
""" Daily Coding Problem #2 - 4/24/2020 """


def array_product(array=[]):
    """
    Create a new array such that each element at the
    current index is the product of all the numbers
    (except itself) in the given array
    Note:
        1. O(n) time complexity
        2. Inspired by Sitesh Roy at
           https://www.geeksforgeeks.org/product-
           array-puzzle-set-2-o1-space/
    Args:
        array: array of numbers
    Return:
        new array: integers of products
    """

    """
    Declare and initialize new array and a variable
    for total product of the whole array
    """
    new_array = []
    product = 1
    for element in array:
        product *= element

    """
    Iterate through array to calculate the power of
    each element.  Then, multiple the result with
    the total product.  This method avoids calculating
    itself and using division.
    1. 120 * (1 ^ -1) = 60
    2. 120 * (2 ^ -1) = 40
    3. 120 * (3 ^ -1) = 30
    4. 120 * (4 ^ -1) = 24
    """
    for element in array:
        power = product * (element ** -1)
        new_array.append(int(power))
    print(new_array)

""" Driver program for testing """
array = [1, 2, 3, 4, 5]
array_product(array)
print("New array returned above")
