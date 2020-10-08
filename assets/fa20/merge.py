import sys
"""
run:

python3 -m doctest -v merge.py

"""

# the following line increases recursion limit (not safe!)
# sys.setrecursionlimit(10000)
# Q4.2 recursive
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
    >>> for _ in range(10): # try changing the input to `range`!
    ...         garbage = next(result)
    """
    def helper(a, b, val_a, val_b):
        if val_a == val_b:
            yield val_a # can yield either val_a or val_b
            yield from helper(a, b, next(a), next(b))
        elif val_a < val_b:
            yield val_a
            yield from helper(a, b, next(a), val_b)
        else:
            yield val_b
            yield from helper(a, b, val_a, next(b))
    yield from helper(a, b, next(a), next(b))

"""
The main problem with making a clean recursive version of merge (with no helper/extra parameters)
is that subsequent recursive frames need additional information from their parent frame. Each successive
recursive call needs to know what the current value in a and b are and without the benefit of sharing a
single frame, extra information needs to be passed from layer to layer.

However, this solution works! ... for small inputs. If you change the argument to the range function on 
line 23 from 10 to a large number like 1000, you'll see that Python will give up and spit out a RecursionError.
There are ways to get around this (see https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it),
but apparently it's not safe and thus not recommended.

To directly address the points brought up today during tutorial:

    Q1: Do generators remember where they left off across function calls (when being passed around as arguments)?
    A1: Yes.

    Q2: Can you write a recursive solution?
    A2: Yes, but it's not especially elegant and definitely not efficient.

    Q3: Does the recursive solution cause a memory leak?
    A3: I don't think so, but I'm not very familiar with memory management in Python. If you're curious though, check out
    this [post](https://medium.com/zendesk-engineering/hunting-for-memory-leaks-in-python-applications-6824d0518774)!
        - I tried some of the memory analysis tools suggested with a recursion limit of 10000 and ended up with these results:
            With range(1000): https://github.com/LarynQi/LarynQi.github.io/raw/master/assets/fa20/memory-profile-1000.png
            With range(10000): https://github.com/LarynQi/LarynQi.github.io/raw/master/assets/fa20/memory-profile-10000.png
        - Verict: doesn't seem like memory leaking is the issue here

    Q4: Can I see an example of a Tree Recursive Generator problem?
    A4: Yes:
        - FA19 MT2 Q5a: https://inst.eecs.berkeley.edu/~cs61a/su20/exam/fa19/mt2/61a-fa19-mt2.pdf#page=6
        - FA19 Final Q4: https://inst.eecs.berkeley.edu/~cs61a/su20/exam/fa19/final/61a-fa19-final.pdf#page=4
        - SU20 HW06 Q6: https://inst.eecs.berkeley.edu/~cs61a/su20/hw/hw06/#q6
            - It's fine to take a look at this one, but I would hold off on doing it right now since there's a 
            decent chance that we'll reuse this problem for a coming HW later this semester.
"""
