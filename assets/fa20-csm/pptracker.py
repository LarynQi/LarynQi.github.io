"""
run:

python3 -m doctest -v pptracker.py

"""

### Anon. Poet Solution ###
class PingPongTracker:

    def __init__(self):
        self.direction = 1
        self.prev = 0


    def next(self):
        self.prev += self.direction
        if has_eight(self.prev) or self.prev % 8 == 0:
            self.direction = self.direction * -1
        return self.prev

# Ping Pong Sequence: 1 2 3 4 5 6 7 [8] 7 6 5 4 3 2 1 [0] 1 [2] 1 0 -1 -2 -3 [-4] -3 -2 -1 [0] -1 -2
def test_tracker():
    """
    >>> tracker1 = PingPongTracker()
    >>> tracker2 = PingPongTracker()
    >>> tracker1.next()
    1
    >>> tracker1.next()
    2
    >>> tracker2.next()
    1
    >>> for _ in range(20):
    ...     tracker1.next()
    3
    4
    5
    6
    7
    8
    7
    6
    5
    4
    3
    2
    1
    0
    1
    2
    1
    0
    -1
    -2
    """
    pass

def has_eight(n):
    if n < 10:
        return n == 8
    return n % 10 == 8 or has_eight(n // 10)

### CSM Solution ###
# class PingPongTracker:
    
#     def __init__(self):
#         self.current = 0
#         self.index = 1
#         self.add = True


#     def next(self):
#         if self.add:
#             self.current += 1
#         else:
#             self.current -= 1
#         if has_eight(self.index) or self.index % 8 == 0:
#             self.add = not self.add
#         self.index += 1
#         return self.current
