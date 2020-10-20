class Baller:
    all_players = []
    def __init__(self, name, has_ball = False):
       self.name = name
       self.has_ball = has_ball
       Baller.all_players.append(self)

    def pass_ball(self, other_player):
       if self.has_ball:
          self.has_ball = False
          other_player.has_ball = True
          return True
       else:
          return False

class BallHog(Baller):
    def pass_ball(self, other_player):
       return False

>>> alina = Baller('Alina', True)
>>> kenny = BallHog('Kenny')
>>> len(Baller.all_players)


class TeamBaller(_______________):
    """
    >>> jamie = BallHog('Jamie')
    >>> cheerballer = TeamBaller('Ethan', has_ball=True)
    >>> cheerballer.pass_ball(jamie)
    Yay!
    True
    >>> cheerballer.pass_ball(jamie)
    I don't have the ball
    False
    """
    def pass_ball(_______________, ________________):


1 2 3 4 5 6 7 [8] 7 6 5 4 3 2 1 [0] 1 [2] 1 0 -1 -2 -3 [-4] -3 -2 -1 [0] -1 -2
>>> tracker1 = PingPongTracker()
>>> tracker2 = PingPongTracker()
>>> tracker1.next()
1
>>> tracker1.next()
2
>>> tracker2.next()
1

class PingPongTracker:
    def __init__(self):






    def next(self):


class Musician:
    popularity = 0
    def __init__(self, instrument):
        self.instrument = instrument
    def perform(self):
        print("a rousing " + self.instrument + " performance")
        self.popularity = self.popularity + 2
    def __repr__(self):
        return self.instrument

class BandLeader(Musician):
    def __init__(self):
        self.band = []
    def recruit(self, musician):
        self.band.append(musician)
    def perform(self, song):
        for m in self.band:
            m.perform()
        Musician.popularity += 1
        print(song)
    def __str__(self):
        return "Here's the band!"
    def __repr__(self):
        band = ""
        for m in self.band:
            band += str(m) + " "
        return band[:-1]

miles = Musician("trumpet")
goodman = Musician("clarinet")
ellington = BandLeader()


class Bird:
    def __init__(self, call):
        self.call = call
        self.can_fly = True
    def fly(self):
        if self.can_fly:
            return "Don't stop me now!"
        else:
            return "Ground control to Major Tom..."
    def speak(self):
        print(self.call)

class Chicken(Bird):
    def speak(self, other):
        Bird.speak(self)
        other.speak()

class Penguin(Bird):
    can_fly = False
    def speak(self):
        call = "Ice to meet you"
        print(call)

andre = Chicken("cluck")
gunter = Penguin("noot")
>>> andre.speak(Bird("coo"))


