"""
run:

python3 -m doctest -v tut05.py

"""

# Q1.3
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                    [tree(2,
    ...                            [tree(3),
    ...                            tree(4)]),
    ...                    tree(5,
    ...                        [tree(6,
    ...                                [tree(7)]),
    ...                        tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    "*** YOUR CODE HERE ***"

# Q1.4
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    "*** UNCOMMENT SKELETON ***"
    # if _____________________________:
    #     return _____________________________
    # _____________________________:
    #     path = _____________________________
    #     if _____________________________:
    #         return _____________________________

# Tree ADT

# Constructor
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selector
def label(tree):
    """Return the label value of a tree."""
    return tree[0]

# Selector
def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

# For convenience
def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise."""
    return not branches(tree)