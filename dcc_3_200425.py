#!/usr/bin/python3
""" Daily Coding Problem #3 - 4/25/2020 """

class Node:
    """ Given Node class for binary tree """
    def __init__(self, val, left=None, right=None):
        """ Method initializing class attributes """
        self.val = val
        self.left = left
        self.right = right

    def serialize(root):
        """
        Method serializes the binary tree into a string
        Note:
            Inspired by https://medium.com/@dimko1/serialize-
            and-deserialize-binary-tree-e9811ead85ed
        Arg:
            root: root to binary tree
        """
        s = str(self.val)

        

    def deserialize(s):
        """
        Method deserializes the string back into a binary tree
        Note:
            Inspired by https://medium.com/@dimko1/serialize-
            and-deserialize-binary-tree-e9811ead85ed
        Arg:
            s: string
        """


""" Driver program for testing """
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
