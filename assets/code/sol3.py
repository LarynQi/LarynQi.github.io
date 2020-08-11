"""
Q3:

Write a function that takes a Tree object and returns the elements at the depth
with the most elements.
In this problem, you may find it helpful to use the second optional argument to sum,
which provides a starting value. All items in the sequence to be summed will be
concatenated to the starting value. By default, start will default to 0, which allows
you to sum a sequence of numbers. We provide an example of sum starting with a
list, which allows you to concatenate items in a list.
"""

def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ... Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while x:
        levels.append([t.label for t in x])
        x = sum([t.branches for t in x], [])
    return max(levels, key=len)

# Tree Class

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)
