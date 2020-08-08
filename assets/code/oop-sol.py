"""
---USAGE---

python3 oop-sol.py <name_of_function>

e.g. python3 oop-sol.py play_round

for classes/methods:
    
class:  python3 oop-sol.py Crooked
method: python3 oop-sol.py IceCream.__init__

---NOTES---

- if you pass all the doctests, you will get no terminal output
    - if you want to see the verbose output (all output shown even if the function is correct), run this:

    python3 oop-sol.py <name_of_function> -v

- if you want to test all of your functions, run this:

    python3 oop-sol.py all

"""

### OOP Topical Review Solutions ### 

#####################
###   Ice Cream   ###
#####################

# Q1a
class IceCream:
    colors = {"strawberry": "pink",
              "chocolate": "brown",
              "pistachio": "green",
              "vanilla": "white",
              "mango": "yellow",
              "mint": "green"
             }
    freezing_point, melting_point = 10, 31
    inventory = {} # An inventory of all available IceCreams. Maps flavors to a list of corresponding IceCreams.

    def __init__(self, flavor, temperature, scoops, new=True):
        """
        >>> len(IceCream.inventory)
        0
        >>> m = IceCream("mango", 25, 5)
        >>> len(IceCream.inventory)
        1
        >>> len(IceCream.inventory["mango"])
        1
        >>> IceCream.inventory["vanilla"]
        Traceback (most recent call last):
            ...
        KeyError: 'vanilla'
        """
        self.flavor = flavor
        self.temperature = temperature
        self.scoops = scoops
        self.eaten = not new
        self.servings = 1
        if flavor not in IceCream.inventory:
            IceCream.inventory[flavor] = []
        IceCream.inventory[flavor].append(self) # (1) Update inventory with this ice cream

    def split(self, ways):
        """Updates SELF.SCOOPS to be the number of scoops per serving.
        Updates SELF.SERVINGS to be the number of servings."""
        self.servings *= ways
        self.scoops /= ways
        print(str(self.servings)
              + " individual(s) get(s) "
              + str(self.scoops)
              + " original scoop(s) each.")

    def freeze(self):
        """
        >>> s = IceCream("strawberry", 20, 2)
        >>> s.freeze()
        >>> s.temperature
        10
        >>> IceCream.freezing_point = -1000
        >>> s.freeze()
        >>> s.temperature
        -1000
        """
        self.temperature = IceCream.freezing_point # (2) Set to freezing point

    def heat(self, degrees):
        """
        >>> s = IceCream("strawberry", 20, 2)
        >>> s.heat(10)
        >>> s.temperature
        30
        >>> s.heat(1)
        Eat me soon, I'm melting!!!
        """
        self.temperature += degrees # (3) Update temperature
        if self.temperature >= IceCream.melting_point:
            print("Eat me soon, I'm melting!!!")

    def melt(self):
        """
        >>> s = IceCream("strawberry", 20, 2)
        >>> s.melt()
        >>> s.temperature
        31
        >>> IceCream.melting_point = 1000
        >>> s.melt()
        >>> s.temperature
        1000
        """
        self.temperature = IceCream.melting_point # (4) Set to melting point

    def remove(self): 
        # (5) Remove this ice cream from the inventory. How do you refer to the inventory?
        IceCream.inventory[self.flavor].remove(self)
        if not self.eaten:
            self.eaten = True
            print("NOM NOM NOM!")
            return True
        else:
            print("Sorry! You thought this " + self.flavor + " ice cream was available but it is not.")
            return False

    def __repr__(self):
        return f"Flavor: {self.flavor}, Temperature: {self.temperature}"

# Q1b
class Eater:

    def __init__(self, name, appetite, favorite, picky=False):
        self.name = name
        self.appetite = appetite
        self.favorite = favorite
        self.picky = picky
        print("I can eat " + str(self.appetite) + " ice creams!")

    def choose(self, craving=False):
        """A picky Eater only eats their favorite ice cream flavor and wants
        the coldest ice cream available. Any other Eater would typically be
        Happy with the coldest ice cream regardless of flavor, unless they
        have a craving. If an Eater has a craving then they behave like a
        picky eater.

        >>> m = IceCream("mint", 25, 5)
        >>> marcus = Eater("Marcus", 1, "mango", picky=True)
        I can eat 1 ice creams!
        >>> marcus.choose()
        Oh no! Your favorite flavor is not available!

        >>> marcus.favorite = "mint"
        >>> marcus.choose()
        Flavor: mint, Temperature: 25

        >>> mark = Eater("Mark", 2, "strawberry")
        I can eat 2 ice creams!
        >>> mark.choose()
        Flavor: mint, Temperature: 25

        >>> IceCream.inventory = {}
        >>> mark.choose()
        """

        if self.picky or craving:
         # (6) How do we know we are out of their favorite flavor? Fill in the conditions.
            if self.favorite not in IceCream.inventory or not IceCream.inventory[self.favorite]: # not IceCream.inventory.get(self.favorite, [])
                print("Oh no! Your favorite flavor is not available!")
                return
            else:
                # (7) If they’re picky or have a craving and we’re *not* out of their
                # favorite flavor, what are their choices? (Hint: CHOICES should be a list)
                choices = IceCream.inventory[self.favorite]
        else:
            choices = []
            # (8) If they’re not picky and do not have a craving, how can you build their
            # list of choices? What can you iterate over in the line below?
            for flavor in IceCream.inventory:
                choices.extend(IceCream.inventory[flavor])
        if choices: # Think about what this condition is checking.
            # (9) Recall that a non-picky and non-craving Eater wants the coldest ice cream
            # regardless of flavor. How do you get the coldest ice cream from CHOICES?
            chosen = min(choices, key=lambda choice: choice.temperature)
            return chosen

    def eat(self, craving=False):
        """An eater can only eat if they have a positive appetite, or in other words, an 
        appetite greater than 0."""

        # (10) What does the docstring above say? Translate that condition to code below.
        if self.appetite > 0:
            ice_cream = self.choose(craving)
            if ice_cream: # This checks that ICE_CREAM is not None
                # (11) What method from the IceCream class should you call below?
                eaten = ice_cream.remove()
                if eaten:
                    print("Mmm... that was such a good "
                          + str(ice_cream.scoops) + " scoops of "
                          + ice_cream.flavor + " ice cream!")
                    self.appetite -= 1 # (12) Update the appetite
                else:
                    print(self.name + " is sad.")
            else:
                print(":'(")
        else:
            print(self.name + " is not hungry anymore!")


# Q1c
def wwpd():
    """
    >>> IceCream.inventory = {}
    >>> s = IceCream("strawberry", 20, 2)
    >>> p = IceCream("pistachio", 35, 3, new=False)
    >>> c = IceCream("chocolate", 10, 15)
    >>> c.split(2)
    2 individual(s) get(s) 7.5 original scoop(s) each.

    >>> rose = Eater("r", 50, "strawberry")
    I can eat 50 ice creams!

    >>> victor = Eater("v", 1, "pistachio", picky=True)
    I can eat 1 ice creams!

    >>> rose.eat()
    NOM NOM NOM!
    Mmm... that was such a good 7.5 scoops of chocolate ice cream!

    >>> rose.eat()
    NOM NOM NOM!
    Mmm... that was such a good 2 scoops of strawberry ice cream!

    >>> rose.eat()
    Sorry! You thought this pistachio ice cream was available but it is not.
    r is sad.

    >>> v = IceCream("vanilla", 20, 3)
    >>> victor.eat()
    Oh no! Your favorite flavor is not available!
    :'(

    >>> p2 = IceCream("pistachio", 15, 3)
    >>> p3 = IceCream("pistachio", 10, 1)
    >>> victor.eat()
    NOM NOM NOM!
    Mmm... that was such a good 1 scoops of pistachio ice cream!

    >>> victor.eat()
    v is not hungry anymore!

    """
    pass

# Q1d
"""
Bonus Question (you can skip this and come back to it later if you have time)

Did you notice how picky Eaters and regular Eaters have different ways to choose their preferred ice cream?
How about instead of using an instance attribute to keep track of whether an Eater is picky,
create a subclass of the Eater class called PickyEater?

i) Which method(s) would you have to override in the PickyEater class?
You only have to override choose in the PickyEater class.

ii) Do we need to have the parameter picky in the __init__ method for Eater? What about for PickyEater?
Depending on how you implement the code, it is possible to eliminate the picky parameter completely.

iii) Try to write the code from scratch below. You can re-write parts of the existing code.
See below for sample code response.

# Modify __init__ and choose methods in Eater class
class Eater:
    def __init__(self, name, appetite, favorite):
        self.name = name
        self.appetite = appetite
        self.favorite = favorite
        print("I can eat " + str(self.appetite) + " ice creams!")

    def choose(self, craving=False):
        # An eater is typically happy with the coldest ice cream regardless of flavor, unless they have a craving. If an Eater has a craving then they behave like a PickyEater.
        if craving:
            return PickyEater.choose(self, craving)
        else:
            choices = []
            for flavor, ice_creams in IceCream.inventory.items():
                choices.extend(ice_creams)
            if choices:
                chosen = min(choices, key=lambda choice: choice.temperature)
                return chosen

# Create PickyEater class and override Eater class’s choose method.
class PickyEater:
    def choose(self, craving=False):
        # A picky eater only eats ice creams of their favorite flavor, and wants the coldest ice cream possible.

        if self.favorite not in IceCream.inventory or not IceCream.inventory[self.favorite]:
            print("Oh no! Your favorite flavor is not available!")
            return
        else:
            choices = IceCream.inventory[self.favorite]
        if choices:
            chosen = min(choices, key=lambda choice: choice.temperature)
            return chosen

"""

#############################
###   Midterm Elections   ###
#############################

# FA18 MT2 Q5: https://cs61a.org/exam/fa18/mt2/61a-fa18-mt2_sol.pdf
# Q2a
"""
Implement the Poll class and the tally function, which takes a choice c
and returns a list describing the number of votes for c. This list contains
pairs, each with a name and the number of times vote was called on that choice
at the Poll with that name. Pairs can be in any order. Assume all Poll instances
have distinct names. Hint: the dictionary get(key, default) method
(MT 2 guide, page 1 top-right) returns the value for a key if it appears
in the dictionary and default otherwise. 
"""
class Poll:
    s = []

    def __init__(self, n):
        self.name = n
        self.votes = {}
        Poll.s.append(self)

    def vote(self, choice):
        self.votes[choice] = self.votes.get(choice, 0) + 1

def tally(c):
    """Tally all votes for a choice c as a list of (poll name, vote count) pairs.
    
    >>> Poll.s = []
    >>> a, b, c = Poll('A'), Poll('B'), Poll('C')
    >>> c.vote('dog')
    >>> a.vote('dog')
    >>> a.vote('cat')
    >>> b.vote('cat')
    >>> a.vote('dog')
    >>> tally('dog')
    [('A', 2), ('C', 1)]
    >>> tally('cat')
    [('A', 1), ('B', 1)]
    """
    return [(p.name, p.votes[c]) for p in Poll.s if c in p.votes]

# Q2b
"""
Implement the vote method of the Crooked class, which only records every other vote call for
each Crooked instance. Only odd numbered calls to vote are recorded, e.g., first, third, fifth, etc.
"""
class Crooked(Poll):
    """A poll that ignores every other call to vote.

    >>> d = Crooked('D')
    >>> for s in ['dog', 'cat', 'dog', 'cat', 'cat']:
    ...     d.vote(s)
    >>> d.votes
    {'dog': 2, 'cat': 1}
    """
    record = True

    def vote(self, choice):
        if self.record:
            Poll.vote(self, choice)
        self.record = not self.record

####################
###   Cucumber   ###
####################

# FA15 Final Q4: http://inst.eecs.berkeley.edu/~cs61a/fa15/assets/pdfs/61a-fa15-final-solution.pdf#page=
"""
Cucumber is a card game. Cards are positive integers (no suits). Players are numbered from 0 up to 
players (0, 1, 2, 3 in a 4-player game). In each Round, the players each play one card,
starting with the starter and in ascending order (player 0 follows player 3 in a 4-player game).
If the card played is as high or higher than the highest card played so far, that player takes control.
The winner is the last player who took control after every player has played once.
Implement Round so that play_round behaves as described in the doctests below.
Part of your score on this question will be assigned based on composition (don’t repeat yourself). 
"""
def play_round(starter, cards): 
    """Play a round and return all winners so far. Cards is a list of pairs. Each (who , card ) 
    pair in cards indicates who plays and what card they play. 

    >>> play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    [1]
    >>> play_round (1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It’s not your turn, player 3
    It’s not your turn, player 0
    The round is over, player 1
    [1, 3]
    >>> play_round(3, [(3, 7), (2, 5), (0, 9)]) # Round is never completed 
    It’s not your turn, player 2
    [1, 3]
    """ 
    r = Round(starter) 
    for who, card in cards: 
        try: r.play(who, card) 
        except AssertionError as e: 
            print(e) 
    return Round.winners

# Q3
class Round:
    players, winners = 4, [] 

    def __init__(self, starter): 
        self.starter, self.player, self.highest = starter, starter , -1 

    def play(self, who, card):
        assert not self.complete(), "The round is over, player " + str(who) 
        assert who == self.player, "It’s not your turn, player " + str(who) 
        self.player = (who + 1) % self.players 
        if card >= self.highest: 
            self.highest, self.control = card, who 
        if self.complete():
            self.winners.append(self.control) 

    def complete(self): 
        return self.player == self.starter and self.highest > -1

##################
###   CS61A+   ###
##################

# SU15 Final Q5: https://61a-su15-website.github.io/assets/pdfs/61a-su15-final-sol.pdf#page=8
# Q4a
"""
The TAs are building a social networking website called CS61A+. The TAs plan to represent the
network in a class called Network that supports the following method:

    add_friend(user1, user2): adds user1 and user2 to each other’s friends lists.
    If user1 or user2 are not in the Network, add them to the dictionary of friends.
    You may assume user1 and user2 are not already friends. 

Help the TAs implement this method to make their social networking website popular!
"""
class Network: 
    """ 
    >>> cs61a_plus = Network()
    >>> cs61a_plus.add_friend('Robert', 'Jeffrey')
    >>> cs61a_plus.friends['Robert']
    ['Jeffrey']
    >>> cs61a_plus.friends['Jeffrey']
    ['Robert']
    >>> cs61a_plus.add_friend('Jessica', 'Robert') 
    >>> cs61a_plus.friends['Robert']
    ['Jeffrey', 'Jessica']
    """ 

    def __init__(self): 
        self.friends = {} # Maps users to a list of their friends 

    def add_friend(self, user1, user2): 
        if user1 not in self.friends:
            self.friends[user1] = []
        if user2 not in self.friends:
            self.friends[user2] = []
        self.friends[user1].append(user2)
        self.friends[user2].append(user1)

        # Q4b
        """
        CS61A+ turns out to be unpopular. To attract more users, the TAs want to implement a feature
        that checks if two users have at most n degrees of separation. Consider the following CS61A+ Network:

            self.friends = { ’Robert’: [’Jeffrey’, ’Jessica’],
            ’Jeffrey’: [’Robert’, ’Jessica’, ’Yulin’],
            ’Jessica’: [’Robert’, ’Jeffrey’, ’Yulin’], 
            ’Yulin’: [’Jeffrey’, ’Jessica’], 
            ’Albert’: []}

        - There are 0 degrees of separation between a person and themselves. 
        - There is 1 degree of separation between Robert and Jeffrey, because they are direct friends.
        - There are 2 degrees of separation between Robert and Yulin:
          (Robert → Jessica → Yulin)

        - The degree of separation between Albert and anyone else is undefined, since Albert has no friends.

        Implement degrees(user1, user2, n), which returns True if user1 and user2 are separated by at most
        n degrees (fewer degrees is okay). You can assume that user1 and user2 are already in the Network.
        """
        def degrees(self, user1, user2, n):
            """In these doctests, assume cs61a_plus is a Network with the dictionary of friends described in the example. 

            >>> cs61a_plus.degrees(’Robert’, ’Yulin’, 2) # Exactly 2 degrees 
            True
            >>> cs61a_plus.degrees(’Robert’, ’Jessica’, 2) # Less than 2 degrees 
            True 
            >>> cs61a_plus.degrees(’Yulin’, ’Robert’, 1) # More than 1 degree 
            False 
            >>> cs61a_plus.degrees(’Robert’, ’Robert’, 2) # 0 degrees
            True 
            >>> cs61a_plus. degrees(’Albert’, ’Jessica’, 10) # No friends! 
            False 
            """ 
            if user1 == user2: 
                return True 
            elif n <= 0:
                return False 
            for friend in self.friends[user1]: 
                if self.degrees(friend, user2, n - 1): 
                    return True 
            return False






### For running tests only. Not part of Review Session content. ###

import doctest
import sys
import argparse

parser = argparse.ArgumentParser(description="Test your work")
parser.add_argument("func", metavar="function_to_test", help="Function to be tested")
parser.add_argument("-v", dest="v", action="store_const", const=True, default=False, help="Verbose output")
args = parser.parse_args()

try:
    if args.func == "all":
        doctest.testmod(verbose=args.v)
    else:
        if '.' in args.func:
            cla, method_name = args.func.split('.')
            import inspect
            try:
                methods = inspect.getmembers(eval(cla), predicate=inspect.isfunction)
            except:
                sys.exit("Invalid Class")
            exists = [m[0] == method_name for m in methods]
            if exists and any(exists):
                doctest.run_docstring_examples(methods[exists.index(True)][1], globals(), verbose=args.v, name=args.func)
            else:
                sys.exit("Invalid Method")
        else:
            doctest.run_docstring_examples(globals()[args.func], globals(), verbose=args.v, name=args.func)
except Exception as e:
    sys.exit("Invalid Arguments")
