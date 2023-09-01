def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1)
    False
    """
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def unique_digits(n):
    """
    >>> unique_digits(8675309)
    7
    >>> unique_digits(13173131)
    3
    >>> unique_digits(101)
    2
    """
    count = 0
    i = 0
    while i <= 9:
        if has_digit(n, i):
            count += 1
        i += 1
    return count


def has_digit(n, k):
    """
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False











