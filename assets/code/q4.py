"""
Q4:

Fill in the classes Emotion, Joy, and Sadness below so that you get the following
output from the Python interpreter.
"""

class Emotion(object):
    """
    >>> Emotion.num
    0
    >>> joy = Joy()
    >>> sadness = Sadness()
    >>> Emotion.num # number of Emotion instances created
    2

    >>> joy.power
    5

    >>> joy.catchphrase() # Print Joy's catchphrase
    Think positive thoughts!

    >>> sadness.catchphrase() # Print Sad's catchphrase
    I'm positive you will get lost.

    >>> sadness.power
    5

    >>> joy.feeling(sadness) # When both Emotions have same power value, print "Together"
    Together

    >>> sadness.feeling(joy)
    Together

    >>> joy.power = 7
    >>> joy.feeling(sadness) # Print the catchphrase of the more powerful feeling before the less powerful feeling
    Think positive thoughts!
    I'm positive you will get lost.

    >>> sadness.feeling(joy)
    Think positive thoughts!
    I'm positive you will get lost.

    """

    num = 0

    def __init__(self):
        ______________
        ______________

    def feeling(self, other):
        if ______________:
            ______________
            ______________
        elif _____________________:
            ______________
            ______________
        else:
            ______________

class Joy(Emotion):

    def catchphrase(self):
        _____________________

class Sadness(Emotion):
    
    def catchphrase(self):
        _____________________
