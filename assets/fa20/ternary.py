
# source: https://www.programiz.com/python-programming/list-comprehension
def ternary(s):
    """
    Negates all the even-indexed elements and doubles the odd-indexed elements.

    >>> lst = [1, 2, 3, 4, 5]
    >>> ternary(lst)
    [-1, 4, -3, 8, -5]
    >>> ternary(range(20))
    [0, 2, -2, 6, -4, 10, -6, 14, -8, 18, -10, 22, -12, 26, -14, 30, -16, 34, -18, 38]
    """
    return [-s[i] if i % 2 == 0 else 2 * s[i] for i in range(len(s))]
