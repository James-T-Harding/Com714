import string
import random as rand

from planet import Planet


def makename():
    inc = 0.2
    conschance = 0.75

    consnts = list(string.ascii_lowercase)
    vowels = ['a', 'e', 'o', 'i', 'u']

    for c in vowels:
        consnts.remove(c)

    ret = ''

    for i in range(rand.randint(2, 10)):
        opt = rand.random() > conschance

        conschance += inc if opt else -inc
        optlist = vowels if opt else consnts

        ret += rand.choice(optlist)

    return ret


class Universe:
    def __init__(self) -> None:
        self.planets = []

    def generate(self) -> Planet:
        planet = Planet(makename())
        self.planets.append(planet)

        return planet

    def __repr__(self):
        return f"Universe({', '.join([repr(p) for p in self.planets])})"

    def __str__(self):
        names = [p.name for p in self.planets]

        return f"A universe of mystery and wonder, consisting of the planets {', '.join(names[:-1])} and {names[-1]}"


u = Universe()

for i in range(5):
    u.generate()

print(repr(u))
