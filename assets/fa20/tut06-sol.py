"""
run:

python3 -m doctest -v tut06-sol.py

"""

# Q2.3
def group_by(s, fn):
    """
    >>> {k: v for k, v in sorted(group_by([12, 23, 14, 45], lambda p: p // 10).items(), key=lambda pair: pair[0])}
    {1: [12, 14], 2: [23], 4: [45]}
    >>> {k: v for k, v in sorted(group_by(range(-3, 4), lambda x: x * x).items(), key=lambda pair: pair[0])}
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    grouped = {}
    for x in s:
        key = fn(x)
        if key in grouped:
            grouped[key].append(x)
        else:
            grouped[key] = [x]
    return grouped

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
    count = 0
    for element in s:
        if element == x:
            count += 1
    while count > 0:
        s.append(el)
        count -= 1

    # Alternate Solution 1:
    # for i in range(len(s)):
    #     if s[i] == x:
    #         s.append(el)

    # Alternate Solution 2:
    # for element in list(s):
    #     if element == x:
    #         s.append(el)

    # Alternate Solution 3:
    # end = len(s)
    # i = 0
    # while i < end:
    #     if s[i] == x:
    #         s.append(el)
    #     i += 1

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
    first_a, first_b = next(a), next(b)
    while True:
        if first_a == first_b:
            yield first_a
            first_a, first_b = next(a), next(b)
        elif first_a < first_b:
            yield first_a
            first_a = next(a)
        else:
            yield first_b
            first_b = next(b)
