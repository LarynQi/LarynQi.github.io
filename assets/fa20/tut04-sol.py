"""
run:

python3 -m doctest -v tut04-sol.py

"""

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    if n < 0 or k < 0:
        return 0
    # ways = 0
    # for step in range(1, k + 1):
    #     ways += count_k(n - step, k)
    # return ways
    return count_k(n - k, k) + count_k(n, k - 1)

# def even_weighted(s):
#     """
#     >>> x = [1, 2, 3, 4, 5, 6]
#     >>> even_weighted(x)
#     [0, 6, 20]
#     """

#     return [s[i] * i for i in range(len(s)) if i % 2 == 0]
