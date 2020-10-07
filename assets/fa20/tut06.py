"""
run:

python3 -m doctest -v tut06.py

"""

# Q2.3
def group_by(s, fn):
    """
    >>> {k: v for k, v in sorted(group_by([12, 23, 14, 45], lambda p: p // 10).items(), key=lambda pair: pair[0])}
    {1: [12, 14], 2: [23], 4: [45]}
    >>> {k: v for k, v in sorted(group_by(range(-3, 4), lambda x: x * x).items(), key=lambda pair: pair[0])}
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    "*** UNCOMMENT SKELETON ***"
    # grouped = {}
    # for ____________________:
    #     key = _________________
    # if ______________________________________:
    #     ____________________________________________
    # else:
    #     grouped[key] = ___________________________________
    # return _________________________________

# Q2.4
def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"

# Q4.2
def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"
