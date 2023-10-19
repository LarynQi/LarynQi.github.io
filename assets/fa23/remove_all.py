def remove_all(link, value):
    """Removes all nodes in link that contain value. The first element of
    link is never equal to value.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> l2 = Link(1, Link(2))
    >>> remove_all(l2, 2)
    >>> print(l2)
    <1>
    >>> l3 = Link.empty
    >>> remove_all(l3, 0)
    >>> print(l3)
    ()
    """
    if link is Link.empty:
        return
    elif link.rest is Link.empty:
        return
    elif link.rest.first == value:
        link.rest = link.rest.rest
        remove_all(link, value)
    else:
        remove_all(link.rest, value)

    """
    # ORIGINAL INCORRECT SOLUTION

    if link is Link.empty:
        return
    elif link.rest is Link.empty:
        return
    elif link.rest.first == value:
        link.rest = link.rest.rest
    remove_all(link.rest, value)
    """


class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
